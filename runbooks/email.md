
# Runbook: Problemas con el correo corporativo

## Objetivo
Diagnosticar y resolver problemas de acceso, envío y recepción
de correos electrónicos corporativos.

## Diagnóstico
1. Verificar que el usuario tenga conexión a Internet.
2. Comprobar si puede acceder al correo desde el navegador.
3. Revisar si el servicio de correo corporativo está disponible.
4. Identificar si el problema afecta a un usuario o a varios.
5. Revisar los mensajes de error y registros disponibles.

## Resolución

### No puede acceder al correo
- Verificar que esté utilizando la dirección corporativa correcta.
- Comprobar si la cuenta está bloqueada.
- Si el problema está relacionado con MFA, seguir el runbook mfa.md.

### No puede enviar correos
- Verificar la conectividad.
- Comprobar si el servicio de envío está disponible.
- Revisar los mensajes de error.

### No recibe correos
- Revisar las carpetas de spam y correo no deseado.
- Comprobar si el buzón alcanzó su límite de almacenamiento.
- Verificar si existen incidentes conocidos del servicio.

## Política de seguridad
- Nunca solicitar ni almacenar contraseñas.
- No pedir códigos MFA ni tokens de acceso.
- No acceder al contenido privado de los correos sin autorización.
- No modificar permisos de cuentas sin aprobación.

## Escalamiento
Escalar al equipo de soporte L2 cuando:
- El problema persiste después del diagnóstico.
- Se detecta una interrupción general del servicio.
- Existen indicios de acceso no autorizado.

Los incidentes relacionados con MFA deben derivarse
al equipo de Identity Management.
