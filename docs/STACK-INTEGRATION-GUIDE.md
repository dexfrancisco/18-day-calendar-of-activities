# Stack Integration Guide

Global skills define quality; the project stack defines implementation.

## React/Next.js + TypeScript + shadcn/ui
Use the existing React/Next conventions, TypeScript when selected, Tailwind when selected, shadcn/ui primitives and Lucide when selected. Do not recreate existing shadcn components. Authoritative business audit should normally be server-side.

## Laravel + Livewire + Flux/Filament
Follow Laravel conventions and selected Livewire/Flux/Filament components. Use policies, middleware, events/listeners, observers or audit services according to existing architecture. Do not introduce React just for components.

## PHP
Follow actual routing/auth/data-access/service architecture and centralize structured audit creation.

## Node/Express
Use request middleware for correlation context and dedicated server/domain audit services.

## Other stacks
Detect and follow the actual stack; do not assume these examples apply.
