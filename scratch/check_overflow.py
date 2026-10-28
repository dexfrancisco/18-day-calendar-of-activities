import subprocess
import json

script = '''
(() => {
    const cards = Array.from(document.querySelectorAll('.day-card, .calendar-canvas, .calendar-main'));
    const overflows = [];
    for (const el of cards) {
        if (el.scrollHeight > el.clientHeight + 2) {
            overflows.push({
                tag: el.className,
                text: el.innerText.slice(0, 40).replace(/\\n/g, ' '),
                scrollHeight: el.scrollHeight,
                clientHeight: el.clientHeight
            });
        }
    }
    return JSON.stringify(overflows);
})()
'''

print("Checking layout overflow in Chrome...")
cmd = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "--headless=new",
    "--disable-gpu",
    "--window-size=4961,3508",
    "--run-all-compositor-stages-before-draw",
    "http://localhost:8991/18-day-campaign-calendar-a3.html"
]

