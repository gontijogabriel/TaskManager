from django.db import models


class BaseModel(models.Model):
	created_at  = models.DateTimeField(verbose_name='Criado em', auto_now_add=True, db_index=True)
	updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

	class Meta:
		abstract = True