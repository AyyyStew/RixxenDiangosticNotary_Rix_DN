from django.db import models

class EntityInfo(models.Model):
	name = models.CharField("Name", max_length=50)
	description = models.CharField("Description", max_length=250)

	class Meta:
		abstract = True

	def __str__(self):
		return self.name

class Topic(EntityInfo):
	pass

class Goal(EntityInfo):
	pass

class Resource(EntityInfo):
	pass

class Measure(EntityInfo):
	pass


class Person(models.Model):
	first_name = models.CharField("First Name", max_length=20)
	middle_name = models.CharField("Middle Name", max_length=20)
	last_name = models.CharField("Last Name", max_length=20)
	date_of_birth = models.DateField("Date of Birth")

	class Meta:
		abstract = True

	def __str__(self) -> str:
		return f"{self.first_name} {self.last_name}"


class Patient(Person):
	notes = models.CharField("Patient Notes",  max_length=500)


class CarePlan(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	topic = models.ForeignKey(Topic, on_delete=models.RESTRICT)
	resources = models.ManyToManyField(Resource)
	measures = models.ManyToManyField(Measure)
	goals = models.ManyToManyField(Goal)

	date = models.DateField()

	def __str__(self) -> str:
		return f"{str(self.patient)} on {self.date}"

