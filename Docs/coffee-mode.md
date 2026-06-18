# Modo Café ☕

- [← Índice](./README.md)
- [Portada](../README.md)

## Qué hace
- Cambia a un tema cálido (“Café”)
- Muestra un overlay centrado con una taza humeante
- **Bloquea toda la UI** hasta que el usuario mueva el ratón o pulse una tecla (o termine el descanso Pomodoro)

## Activación
- Botón **☕** en la barra superior
- Atajo: `Ctrl+Alt+C`
- **Pomodoro automático**: al llegar a cero la cuenta atrás de trabajo (si está configurado)

## Personalización
Abre **Preferencias** (`Ctrl+,` o Activity Bar → Settings) → pestaña **☕ Café**:

| Opción | Descripción | Valor por defecto |
|--------|-------------|-------------------|
| Mensaje | Texto en el overlay durante la pausa | *Mueve el ratón o pulsa cualquier tecla para volver.* |
| Pomodoro automático | Descansos programados cada X minutos | Desactivado |
| Intervalo de trabajo | Minutos hasta el próximo descanso | 25 min |
| Duración del descanso | Minutos con cuenta atrás en el overlay | 5 min |

## Pomodoro 🍅
Con Pomodoro activo:
1. En la **barra de estado** verás `☕ MM:SS` con el tiempo restante hasta el próximo descanso.
2. Al llegar a cero se activa el Modo Café automáticamente.
3. En el overlay aparece **Descanso: MM:SS** descontando el tiempo de pausa.
4. Puedes salir antes moviendo el ratón o pulsando una tecla; al terminar el tiempo, el overlay se cierra solo y reinicia el ciclo de trabajo.
5. El botón ☕ y `Ctrl+Alt+C` siguen funcionando para pausas manuales (con el mismo temporizador de descanso si Pomodoro está activo).

Sin Pomodoro, el Modo Café manual funciona igual que antes: overlay con tu mensaje personalizado, sin temporizadores.

## Ver también
- [Atajos de teclado](./shortcuts.md)
- [Interfaz del editor (status bar y botón ☕)](./editor-interface.md)
- [Archivos, pestañas y explorador](./files-and-tabs.md)
