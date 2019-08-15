import graphene

from graphene_django.types import DjangoObjectType
from occupation.models import Occupation

class OccupationType(DjangoObjectType):
    class Meta:
        model = Occupation

class OccupationQuery(graphene.ObjectType):
    getOccupation = graphene.Field(OccupationType, 
                                   occupationId=graphene.Int(required=True))
    getOccupations = graphene.List(OccupationType)

    def resolve_getOccupation(self, info, occupationId):
        return Occupation.objects.filter(pk=occupationId).first()

    def resolve_getOccupations(self, info):
        return Occupation.objects.all()

class OccupationMutation(graphene.ObjectType):
    addOccupation = graphene.Field(OccupationType,
                                   name=graphene.String(required=True), 
                                   companyName=graphene.String(required=True), 
                                   positionName=graphene.String(required=True), 
                                   hireDate=graphene.Date(required=True), 
                                   fireDate=graphene.Date(required=False), 
                                   salary=graphene.Int(required=True), 
                                   fraction=graphene.Int(required=True), 
                                   base=graphene.Int(required=True), 
                                   advance=graphene.Int(required=True), 
                                   by_hours=graphene.Boolean(required=True))

    def resolve_addOccupation(self, info, name, companyName, positionName, hireDate, fireDate, salary, fraction, base, advance, by_hours):
        occupation = Occupation()
        occupation.name = name
        occupation.companyName = companyName
        occupation.positionName = positionName
        occupation.hireDate = hireDate
        occupation.fireDate = fireDate
        occupation.salary = salary
        occupation.fraction = fraction
        occupation.base = base
        occupation.advance = advance
        occupation.by_hours = by_hours
        occupation.save()
        return occupation

schema = graphene.Schema(query=OccupationQuery, mutation=OccupationMutation)
