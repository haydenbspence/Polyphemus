from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional

class Person(BaseModel):
    person_id: int = Field(..., alias='person_id')
    gender_concept_id: int = Field(..., alias='gender_concept_id')
    year_of_birth: int = Field(..., alias='year_of_birth')
    month_of_birth: Optional[int] = None
    day_of_birth: Optional[int] = None
    birth_datetime: Optional[datetime] = None
    race_concept_id: int
    ethnicity_concept_id: int
    location_id: Optional[int] = None
    provider_id: Optional[int] = None
    care_site_id: Optional[int] = None
    person_source_value: str
    gender_source_value: Optional[str] = None
    gender_source_concept_id: Optional[int] = None
    race_source_value: Optional[str] = None
    race_source_concept_id: Optional[int] = None
    ethnicity_source_value: Optional[str] = None
    ethnicity_source_concept_id: Optional[int] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class ObservationPeriod(BaseModel):
    observation_period_id: int
    person_id: int
    observation_period_start_date: date
    observation_period_end_date: date
    period_type_concept_id: int

class VisitOccurrence(BaseModel):
    visit_occurrence_id: int
    person_id: int
    visit_concept_id: int
    visit_start_date: date
    visit_start_datetime: Optional[datetime]
    visit_end_date: date
    visit_end_datetime: Optional[datetime]
    visit_type_concept_id: int
    provider_id: Optional[int]
    care_site_id: Optional[int]
    visit_source_value: Optional[str]
    visit_source_concept_id: Optional[int]
    admitted_from_concept_id: Optional[int]
    admitted_from_source_value: Optional[str]
    discharged_to_concept_id: Optional[int]
    discharged_to_source_value: Optional[str]
    preceding_visit_occurrence_id: Optional[int]

class VisitDetail(BaseModel):
    visit_detail_id: int
    visit_occurrence_id: int
    provider_id: Optional[int]
    visit_start_date: date
    visit_start_datetime: Optional[datetime]
    visit_end_date: date
    visit_end_datetime: Optional[datetime]
    visit_type_concept_id: int
    visit_source_value: Optional[str]
    visit_source_concept_id: Optional[int]
    admitting_source_concept_id: Optional[int]
    admitting_source_value: Optional[str]
    discharge_to_concept_id: Optional[int]
    discharge_to_source_value: Optional[str]
    preceding_visit_detail_id: Optional[int]

class ConditionOccurrence(BaseModel):
    condition_occurrence_id: int
    person_id: int
    condition_concept_id: int
    condition_start_date: date
    condition_start_datetime: Optional[datetime]
    condition_end_date: date
    condition_end_datetime: Optional[datetime]
    condition_type_concept_id: int
    stop_reason: Optional[str]
    provider_id: Optional[int]
    visit_occurrence_id: Optional[int]
    visit_detail_id: Optional[int]
    condition_source_value: Optional[str]
    condition_source_concept_id: Optional[int]
    condition_status_source_value: Optional[str]
    condition_status_concept_id: Optional[int]

class DrugExposure(BaseModel):
    drug_exposure_id: int
    person_id: int
    drug_concept_id: int
    drug_exposure_start_date: date
    drug_exposure_start_datetime: Optional[datetime]
    drug_exposure_end_date: date
    drug_exposure_end_datetime: Optional[datetime]
    verbatim_end_date: Optional[date]
    drug_type_concept_id: int
    stop_reason: Optional[str]
    refills: Optional[int]
    quantity: Optional[int]
    days_supply: Optional[int]
    sig: Optional[str]
    route_concept_id: Optional[int]
    lot_number: Optional[str]
    provider_id: Optional[int]
    visit_occurrence_id: Optional[int]
    visit_detail_id: Optional[int]
    drug_source_value: Optional[str]
    drug_source_concept_id: Optional[int]
    route_source_value: Optional[str]
    dose_unit_source_value: Optional[str]

class ProcedureOccurrence(BaseModel):
   procedure_occurrence_id: int
   person_id: int
   procedure_concept_id: int
   procedure_date: date
   procedure_datetime: Optional[datetime]
   procedure_type_concept_id: int
   modifier_concept_id: Optional[int]
   quantity: Optional[int]
   provider_id: Optional[int]
   visit_occurrence_id: Optional[int]
   visit_detail_id: Optional[int]
   procedure_source_value: Optional[str]
   procedure_source_concept_id: Optional[int]
   qualifier_source_value: Optional[str]

class DeviceExposure(BaseModel):
   device_exposure_id: int
   person_id: int
   device_concept_id: int
   device_exposure_start_date: date
   device_exposure_start_datetime: Optional[datetime]
   device_exposure_end_date: date
   device_exposure_end_datetime: Optional[datetime]
   device_type_concept_id: int
   unique_device_id: Optional[str]
   quantity: Optional[int]
   provider_id: Optional[int]
   visit_occurrence_id: Optional[int]
   visit_detail_id: Optional[int]
   device_source_value: Optional[str]
   device_source_concept_id: Optional[int]

class Measurement(BaseModel):
   measurement_id: int
   person_id: int
   measurement_concept_id: int
   measurement_date: date
   measurement_datetime: Optional[datetime]
   measurement_type_concept_id: int
   operator_concept_id: Optional[int]
   value_as_number: Optional[float]
   value_as_concept_id: Optional[int]
   unit_concept_id: Optional[int]
   range_low: Optional[float]
   range_high: Optional[float]
   provider_id: Optional[int]
   visit_occurrence_id: Optional[int]
   visit_detail_id: Optional[int]
   measurement_source_value: Optional[str]
   measurement_source_concept_id: Optional[int]
   unit_source_value: Optional[str]
   value_source_value: Optional[str]

class Observation(BaseModel):
   observation_id: int
   person_id: int
   observation_concept_id: int
   observation_date: date
   observation_datetime: Optional[datetime]
   observation_type_concept_id: int
   value_as_number: Optional[float]
   value_as_string: Optional[str]
   value_as_concept_id: Optional[int]
   qualifier_concept_id: Optional[int]
   unit_concept_id: Optional[int]
   provider_id: Optional[int]
   visit_occurrence_id: Optional[int]
   visit_detail_id: Optional[int]
   observation_source_value: Optional[str]
   observation_source_concept_id: Optional[int]
   unit_source_value: Optional[str]
   qualifier_source_value: Optional[str]

class Death(BaseModel):
    person_id: int
    death_date: date
    death_datetime: Optional[datetime]
    death_type_concept_id: int
    cause_concept_id: Optional[int]
    cause_source_value: Optional[str]
    cause_source_concept_id: Optional[int]

class Note(BaseModel):
    note_id: int
    person_id: int
    note_date: date
    note_datetime: Optional[datetime]
    note_type_concept_id: int
    note_class_concept_id: int
    note_title: Optional[str]
    note_text: Optional[str]
    encoding_concept_id: Optional[int]
    language_concept_id: Optional[int]
    provider_id: Optional[int]
    visit_occurrence_id: Optional[int]
    visit_detail_id: Optional[int]
    note_source_value: Optional[str]

class NoteNlp(BaseModel):
    note_nlp_id: int
    note_id: int
    section_concept_id: int
    snippet: Optional[str]
    offset: Optional[int]
    lexical_variant: Optional[str]
    note_nlp_concept_id: Optional[int]
    note_nlp_source_concept_id: Optional[int]
    nlp_system: Optional[str]
    nlp_date: Optional[date]
    nlp_datetime: Optional[datetime]
    term_exists: Optional[str]
    term_temporal: Optional[str]
    term_modifiers: Optional[str]

class Specimen(BaseModel):
    specimen_id: int
    person_id: int
    specimen_concept_id: int
    specimen_type_concept_id: int
    specimen_date: date
    specimen_datetime: Optional[datetime]
    quantity: Optional[float]
    unit_concept_id: Optional[int]
    anatomic_site_concept_id: Optional[int]
    disease_status_concept_id: Optional[int]
    specimen_source_id: Optional[str]
    specimen_source_value: Optional[str]
    unit_source_value: Optional[str]
    anatomic_site_source_value: Optional[str]
    disease_status_source_value: Optional[str]

class FactRelationship(BaseModel):
    domain_concept_id_1: int
    fact_id_1: int
    domain_concept_id_2: int
    fact_id_2: int
    relationship_concept_id: int

class Location(BaseModel):
    location_id: int
    address_1: Optional[str]
    address_2: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    county: Optional[str]
    location_source_value: Optional[str]

class CareSite(BaseModel):
    care_site_id: int
    care_site_name: Optional[str]
    place_of_service_concept_id: Optional[int]
    location_id: Optional[int]
    care_site_source_value: Optional[str]
    place_of_service_source_value: Optional[str]

class Provider(BaseModel):
    provider_id: int
    provider_name: Optional[str]
    npi: Optional[str]
    dea: Optional[str]
    specialty_concept_id: Optional[int]
    care_site_id: Optional[int]
    year_of_birth: Optional[int]
    gender_concept_id: Optional[int]
    provider_source_value: Optional[str]
    specialty_source_value: Optional[str]
    specialty: Optional[str]

class PayerPlanPeriod(BaseModel):
    payer_plan_period_id: int
    person_id: int
    payer_plan_period_start_date: date
    payer_plan_period_end_date: date
    payer_concept_id: Optional[int]
    payer_source_value: Optional[str]
    payer_source_concept_id: Optional[int]
    plan_concept_id: Optional[int]
    plan_source_value: Optional[str]
    plan_source_concept_id: Optional[int]
    sponsor_concept_id: Optional[int]
    sponsor_source_value: Optional[str]
    sponsor_source_concept_id: Optional[int]
    family_source_value: Optional[str]
    stop_reason_concept_id: Optional[int]
    stop_reason_source_value: Optional[str]
    stop_reason_source_concept_id: Optional[int]

class Cost(BaseModel):
    cost_id: int
    cost_event_id: int
    cost_domain_id: str
    cost_type_concept_id: int
    currency_concept_id: Optional[int]
    total_charge: Optional[float]
    total_cost: Optional[float]
    total_paid: Optional[float]
    paid_by_payer: Optional[float]
    paid_by_patient: Optional[float]
    paid_patient_copay: Optional[float]
    paid_patient_coinsurance: Optional[float]
    paid_patient_deductible: Optional[float]
    paid_by_primary: Optional[float]
    paid_ingredient_cost: Optional[float]
    paid_dispensing_fee: Optional[float]
    payer_plan_period_id: Optional[int]
    amount_allowed: Optional[float]
    revenue_code_concept_id: Optional[int]
    revenue_code_source_value: Optional[str]
    drg_concept_id: Optional[int]
    drg_source_value: Optional[str]

class DrugEra(BaseModel):
    drug_era_id: int
    person_id: int
    drug_concept_id: int
    drug_era_start_date: date
    drug_era_end_date: date
    drug_exposure_count: Optional[int]
    gap_days: Optional[int]

class DoseEra(BaseModel):
    dose_era_id: int
    person_id: int
    drug_concept_id: int
    unit_concept_id: int
    dose_value: float
    dose_era_start_date: date
    dose_era_end_date: date

class ConditionEra(BaseModel):
    condition_era_id: int
    person_id: int
    condition_concept_id: int
    condition_era_start_date: date
    condition_era_end_date: date
    condition_occurrence_count: Optional[int]

class Episode(BaseModel):
    episode_id: int
    person_id: int
    episode_concept_id: int
    episode_start_date: date
    episode_start_datetime: Optional[datetime]
    episode_end_date: Optional[date]
    episode_end_datetime: Optional[datetime]
    episode_parent_id: Optional[int]
    episode_number: Optional[int]
    episode_object_concept_id: int
    episode_type_concept_id: int
    episode_source_value: Optional[str]
    episode_source_concept_id: Optional[int]

class EpisodeEvent(BaseModel):
    episode_id: int
    event_id: int
    episode_event_field_concept_id: int

class Metadata(BaseModel):
    metadata_id: int
    metadata_concept_id: int
    metadata_type_concept_id: int
    name: str
    value_as_string: Optional[str]
    value_as_concept_id: Optional[int]
    value_as_number: Optional[float]
    metadata_date: Optional[date]
    metadata_datetime: Optional[datetime]

class CdmSource(BaseModel):
    cdm_source_name: str
    cdm_source_abbreviation: str
    cdm_holder: str
    source_description: Optional[str]
    source_documentation_reference: Optional[str]
    cdm_etl_reference: Optional[str]
    source_release_date: date
    cdm_release_date: date
    cdm_version: Optional[str]
    cdm_version_concept_id: int
    vocabulary_version: str

class Concept(BaseModel):
    concept_id: int
    concept_name: str
    domain_id: str
    vocabulary_id: str
    concept_class_id: str
    standard_concept: Optional[str]
    concept_code: str
    valid_start_date: date
    valid_end_date: date
    invalid_reason: Optional[str]

class Vocabulary(BaseModel):
    vocabulary_id: str
    vocabulary_name: str
    vocabulary_reference: Optional[str]
    vocabulary_version: Optional[str]
    vocabulary_concept_id: int

class Domain(BaseModel):
    domain_id: str
    domain_name: str
    domain_concept_id: int

class ConceptClass(BaseModel):
    concept_class_id: str
    concept_class_name: str
    concept_class_concept_id: int

class ConceptRelationship(BaseModel):
    concept_id_1: int
    concept_id_2: int
    relationship_id: int
    valid_start_date: date
    valid_end_date: date
    invalid_reason: Optional[str]

class Relationship(BaseModel):
    relationship_id: int
    relationship_name: str
    is_hierarchical: int
    defines_ancestry: int
    reverse_relationship_id: Optional[int]
    relationship_concept_id: int

class ConceptSynonym(BaseModel):
    concept_id: int
    concept_synonym_name: str
    language_concept_id: int
    valid_start_date: date
    valid_end_date: date
    invalid_reason: Optional[str]

class ConceptAncestor(BaseModel):
    ancestor_concept_id: int
    descendant_concept_id: int
    minimum_levels_of_separation: int
    maximum_levels_of_separation: int

class SourceToConceptMap(BaseModel):
    source_code: Optional[str]
    source_concept_id: Optional[int]
    source_vocabulary_id: str
    source_code_description: Optional[str]
    target_concept_id: int
    target_vocabulary_id: str
    valid_start_date: date
    valid_end_date: date
    invalid_reason: Optional[str]

class DrugStrength(BaseModel):
    drug_concept_id: int
    ingredient_concept_id: int
    amount_value: float
    amount_unit_concept_id: int
    numerator_value: Optional[float]
    numerator_unit_concept_id: Optional[int]
    denominator_value: Optional[float]
    denominator_unit_concept_id: Optional[int]
    box_size: Optional[int]
    valid_start_date: date
    valid_end_date: date
    invalid_reason: Optional[str]

class Cohort(BaseModel):
    cohort_id: int
    cohort_name: str
    cohort_concept_id: int

class CohortDefinition(BaseModel):
    cohort_definition_id: int
    cohort_definition_name: str
    cohort_definition_description: Optional[str]
    definition_type_concept_id: int
    cohort_definition_syntax: Optional[str]
    subject_concept_id: int
    cohort_initiation_date: date
