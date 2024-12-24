# Vehicle Management Module

## Descripción
Este módulo gestiona los vehículos de la empresa, incluyendo información sobre el nombre, la placa, el tipo de combustible, el kilometraje, la última fecha de servicio y si necesita servicio.

## Historial de Modificaciones

### Versión 17.0.1.0.0
- **Fecha:** 2024-12-24
- **Autor:** Robinson Torres
- **Descripción:**
  - Creación inicial del módulo `vehicle_management`.
  - Definición del modelo `my.company.vehicle` con los campos:
    - `name`
    - `license_plate`
    - `fuel_type`
    - `mileage`
    - `last_service_date`
    - `needs_service`
    - `partner_id`
  - Implementación de la lógica para calcular `needs_service` usando `@api.depends`.
  - Implementación de `onchange` en el campo `fuel_type` para establecer `mileage` a 0 si el tipo de combustible es `electric`.
  - Creación de vistas para el modelo `my.company.vehicle`:
    - Vista Kanban mostrando `name`, `license_plate` y `needs_service`.
    - Vista Form organizada en dos columnas y con un botón "Schedule Service".
    - Vista Tree mostrando `name`, `license_plate` y `needs_service`.
    - Vista Search con un filtro para `needs_service`.
  - Creación de reglas de seguridad:
    - Permitir a los usuarios del grupo "Vehicle Manager" ver, crear, editar y eliminar todos los registros.
    - Permitir a los usuarios sin el grupo "Vehicle Manager" solo leer los registros.
  - Creación de un menú bajo "Fleet Management" llamado "Vehicles", visible solo para el grupo "Vehicle Manager".

## Instalación
1. Clonar el repositorio en el directorio de addons de Odoo.
2. Reiniciar el servidor de Odoo.
3. Instalar el módulo `vehicle_management` desde la interfaz de Odoo.

## Uso
- Navegar a "Fleet Management" > "Vehicles" para gestionar los vehículos.
- Los usuarios del grupo "Vehicle Manager" tienen permisos completos sobre los registros de vehículos.
- Los usuarios sin el grupo "Vehicle Manager" solo pueden leer los registros de vehículos.
