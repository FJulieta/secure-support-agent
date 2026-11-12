
# Runbook: Problemas con MFA

## Objetivo
Resolver incidentes relacionados con la autenticación
multifactor de usuarios corporativos.

## Diagnóstico
1. Verificar si el usuario puede acceder a su cuenta.
2. Comprobar si recibe las notificaciones de MFA.
3. Revisar si el dispositivo de autenticación está disponible.
4. Consultar los registros de autenticación para identificar errores.

## Resolución
Si el usuario no recibe notificaciones MFA,
verificar la conectividad del dispositivo.

Si el usuario perdió acceso a su dispositivo MFA,
derivar el caso al equipo de Identity Management.

## Política de seguridad
Nunca solicitar contraseñas, códigos MFA,
tokens de acceso ni códigos de recuperación.

No desactivar MFA sin seguir el procedimiento
de verificación de identidad autorizado.

## Escalamiento
Escalar al equipo de Identity Management cuando:
- El usuario perdió su dispositivo MFA.
- Se detectan intentos de autenticación sospechosos.
- El problema persiste después del diagnóstico.
