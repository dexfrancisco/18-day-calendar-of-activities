Add-Type -AssemblyName PresentationCore
Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class FontInstaller {
    [DllImport("gdi32.dll", EntryPoint = "AddFontResourceW", SetLastError = true)]
    public static extern int AddFontResource([In, MarshalAs(UnmanagedType.LPWStr)] string lpFileName);

    [DllImport("user32.dll", SetLastError = true)]
    public static extern IntPtr SendMessageTimeout(
        IntPtr hWnd,
        uint Msg,
        IntPtr wParam,
        IntPtr lParam,
        uint fuFlags,
        uint uTimeout,
        out IntPtr lpdwResult
    );
}
"@

$sourceDir = "c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity\Gotham-font-family"
$destDir = "$env:LOCALAPPDATA\Microsoft\Windows\Fonts"
$regKey = "HKCU:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts"

if (-not (Test-Path $destDir)) {
    New-Item -Path $destDir -ItemType Directory -Force | Out-Null
}

$fontFiles = Get-ChildItem -Path $sourceDir -Recurse -File -Filter "*.otf"
Write-Host "Found $($fontFiles.Count) OTF font files to install."

$successCount = 0
$failCount = 0
$installedList = @()

foreach ($fontFile in $fontFiles) {
    try {
        # 1. Get exact Font Family and Subfamily/Face names
        $uri = New-Object System.Uri($fontFile.FullName)
        $gt = New-Object System.Windows.Media.GlyphTypeface($uri)
        $win32Fam = ($gt.Win32FamilyNames.Values | Select-Object -First 1)
        $win32Face = ($gt.Win32FaceNames.Values | Select-Object -First 1)
        
        if ($win32Face -and $win32Face -ne "Regular") {
            $fontTitle = "$win32Fam $win32Face"
        } else {
            $fontTitle = $win32Fam
        }

        # 2. Copy font file to User Fonts directory
        $destPath = Join-Path -Path $destDir -ChildPath $fontFile.Name
        Copy-Item -Path $fontFile.FullName -Destination $destPath -Force

        # 3. Register font in Registry (HKCU)
        $regName = "$fontTitle (TrueType)"
        Set-ItemProperty -Path $regKey -Name $regName -Value $destPath -Force

        # 4. Notify GDI of the new font resource immediately
        [FontInstaller]::AddFontResource($destPath) | Out-Null

        $successCount++
        $installedList += [PSCustomObject]@{
            File = $fontFile.Name
            Title = $fontTitle
        }
    } catch {
        Write-Warning "Failed to install $($fontFile.Name): $_"
        $failCount++
    }
}

# 5. Broadcast WM_FONTCHANGE to all top-level windows
Write-Host "Broadcasting WM_FONTCHANGE..."
$HWND_BROADCAST = [IntPtr]0xffff
$WM_FONTCHANGE = 0x001D
$SMTO_ABORTIFHUNG = 0x0002
$result = [IntPtr]::Zero
[FontInstaller]::SendMessageTimeout($HWND_BROADCAST, $WM_FONTCHANGE, [IntPtr]::Zero, [IntPtr]::Zero, $SMTO_ABORTIFHUNG, 2000, [ref]$result) | Out-Null

Write-Host "Installation completed successfully!"
Write-Host "Installed: $successCount"
Write-Host "Failed: $failCount"
