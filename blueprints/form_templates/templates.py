from launch.blueprints.form_templates.TA6_part_1.TA6_part_1 import TA6_Part_1
from launch.blueprints.form_templates.micro_forms.subsidence.subsidence import (
    subsidence,
)
from launch.blueprints.form_templates.micro_forms.sewage_waste_freeholder.sewage_waste_freeholder import (
    sewage_waste_freeholder,
)
from launch.blueprints.form_templates.micro_forms.attic.attic_development.attic_development import (
    attic_development,
)
from launch.blueprints.form_templates.value_controllers import controllers

templates = {
    "TA6_Part_1": TA6_Part_1,
    "subsidence": subsidence,
    "attic_development": attic_development,
    "controllers": controllers,
    "sewage_waste_freeholder": sewage_waste_freeholder,
}
