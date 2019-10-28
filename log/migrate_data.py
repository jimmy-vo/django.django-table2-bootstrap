def populate(apps, schema_editor):
    print("___populate log_type___")
    LogType = apps.get_model('log', 'LogType')

    backend = LogType.objects.get_or_create(id=1)[0]
    backend.name = "Backend"
    backend.save()

    api = LogType.objects.get_or_create(id=2)[0]
    api.name = "Api"
    api.save()
