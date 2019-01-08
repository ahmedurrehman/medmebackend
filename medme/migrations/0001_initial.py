# Generated by Django 2.1.4 on 2018-12-30 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('potency', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('address', models.TextField(default='', max_length=100)),
                ('extra', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('created', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('form', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='medicines', to='medme.Company')),
                ('drugs', models.ManyToManyField(related_name='drugs', through='medme.Composition', to='medme.Drug')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='medicines', to='medme.Form')),
            ],
            options={
                'ordering': ('name', 'created'),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderNumber', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('address', models.TextField(default='')),
                ('status', models.CharField(choices=[('NOT_CONFIRMED', 'Not Confirmed'), ('IN_PROGRESS', 'In Progress'), ('DELIVERED', 'Delivered'), ('COMPLETED', 'Completed')], default='NOT_CONFIRMED', max_length=20)),
                ('productCharges', models.IntegerField(default=0)),
                ('deliveryCharges', models.IntegerField(default=0)),
                ('extraCharges', models.IntegerField(default=0)),
                ('totalBill', models.IntegerField(default=0)),
                ('paymentReceived', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='medme.Customer')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medme.Medicine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medme.Order')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(related_name='items', through='medme.OrderItems', to='medme.Medicine'),
        ),
        migrations.AddField(
            model_name='composition',
            name='drug',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medme.Drug'),
        ),
        migrations.AddField(
            model_name='composition',
            name='medicine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medme.Medicine'),
        ),
    ]
