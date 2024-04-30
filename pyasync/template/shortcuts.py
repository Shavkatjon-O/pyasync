import os


async def render(template_name, context):
    template_path = os.path.join("templates", template_name)

    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    for key, value in context.items():
        template = template.replace("{{ " + key + " }}", value)

    return template
