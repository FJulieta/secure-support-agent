
# Runbook: Problemas de conectividad de red

## Objetivo
Diagnosticar problemas de conectividad en equipos
conectados a la red corporativa.

## Diagnóstico
1. Verificar si el equipo está conectado mediante Wi-Fi o Ethernet.
2. Comprobar si otros dispositivos presentan el mismo problema.
3. Revisar si el equipo tiene una dirección IP asignada.
4. Verificar la conectividad con la puerta de enlace predeterminada.
5. Comprobar la resolución DNS.
6. Revisar si existe una interrupción conocida del servicio de red.

## Resolución

### Sin conexión a Internet
- Verificar el estado de la conexión Wi-Fi o Ethernet.
- Comprobar que el adaptador de red esté habilitado.
- Revisar si el equipo recibió una configuración IP válida.

### Problemas de DNS
- Comprobar si el equipo puede acceder a servicios mediante IP.
- Verificar la configuración de los servidores DNS corporativos.
- No modificar servidores DNS sin autorización.

### Problemas de conectividad interna
- Verificar si el problema afecta a un único equipo.
- Comprobar la disponibilidad de la puerta de enlace.
- Revisar los mensajes de error de conexión.

## Política de seguridad
- No solicitar contraseñas de redes corporativas.
- No desactivar firewalls ni controles de seguridad.
- No modificar configuraciones de red sin autorización.
- No compartir información sensible de infraestructura.

## Escalamiento
Escalar al equipo de Redes o soporte L2 cuando:
- La interrupción afecta a múltiples usuarios.
- Se detecta una falla de infraestructura.
- El problema persiste después de las verificaciones.
- Se sospecha un incidente de seguridad.
