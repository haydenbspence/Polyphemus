# models.py

from pydantic import BaseModel, Field, ValidationError
from typing import Optional, Type
from datetime import datetime, date
import pandas as pd
import numpy as np


def validate_dataframe(df: pd.DataFrame, model: Type[BaseModel]) -> pd.DataFrame:
    for index, row in df.iterrows():
        try:
            # Convert values to None if they are NaN or None
            row_dict = {k: v if not pd.isna(v) and v is not None else None for k, v in row.to_dict().items()}
            model(**row_dict)
        except ValidationError as e:
            print(f"Validation error for row {index}: {e}")
    return df

class Person(BaseModel):
    person_id: int = Field(..., alias='PERSON_ID')
    gender_concept_id: int = Field(..., alias='GENDER_CONCEPT_ID')
    year_of_birth: int = Field(..., alias='YEAR_OF_BIRTH')
    month_of_birth: Optional[int] = Field(None, alias='MONTH_OF_BIRTH')
    day_of_birth: Optional[int] = Field(None, alias='DAY_OF_BIRTH')
    birth_datetime: Optional[datetime] = Field(None, alias='BIRTH_DATETIME')
    race_concept_id: int = Field(..., alias='RACE_CONCEPT_ID')
    ethnicity_concept_id: int = Field(..., alias='ETHNICITY_CONCEPT_ID')
    location_id: Optional[int] = Field(None, alias='LOCATION_ID')
    provider_id: Optional[int] = Field(None, alias='PROVIDER_ID')
    care_site_id: Optional[int] = Field(None, alias='CARE_SITE_ID')
    person_source_value: str = Field(..., alias='PERSON_SOURCE_VALUE')
    gender_source_value: Optional[str] = Field(None, alias='GENDER_SOURCE_VALUE')
    gender_source_concept_id: Optional[int] = Field(None, alias='GENDER_SOURCE_CONCEPT_ID')
    race_source_value: Optional[str] = Field(None, alias='RACE_SOURCE_VALUE')
    race_source_concept_id: Optional[int] = Field(None, alias='RACE_SOURCE_CONCEPT_ID')
    ethnicity_source_value: Optional[str] = Field(None, alias='ETHNICITY_SOURCE_VALUE')
    ethnicity_source_concept_id: Optional[int] = Field(None, alias='ETHNICITY_SOURCE_CONCEPT_ID')

class Person(BaseModel):
    person_id: Optional[str] = Field(..., alias='PERSON_ID')
    gender_concept_id: Optional[str] = Field(..., alias='GENDER_CONCEPT_ID')
    year_of_birth: Optional[str] = Field(..., alias='YEAR_OF_BIRTH')
    month_of_birth: Optional[str] = Field(..., alias='MONTH_OF_BIRTH')
    day_of_birth: Optional[str] = Field(..., alias='DAY_OF_BIRTH')
    birth_datetime: Optional[datetime] = Field(None, alias='BIRTH_DATETIME')
    race_concept_id: Optional[str] = Field(..., alias='RACE_CONCEPT_ID')
    ethnicity_concept_id: Optional[str] = Field(..., alias='ETHNICITY_CONCEPT_ID')
    location_id: Optional[str] = Field(..., alias='LOCATION_ID')
    provider_id: Optional[str] = Field(..., alias='PROVIDER_ID')
    care_site_id: Optional[str] = Field(..., alias='CARE_SITE_ID')
    person_source_value: Optional[str] = Field(..., alias='PERSON_SOURCE_VALUE')
    gender_source_value: Optional[str] = Field(..., alias='GENDER_SOURCE_VALUE')
    gender_source_concept_id: Optional[str] = Field(..., alias='GENDER_SOURCE_CONCEPT_ID')
    race_source_value: Optional[str] = Field(..., alias='RACE_SOURCE_VALUE')
    race_source_concept_id: Optional[str] = Field(..., alias='RACE_SOURCE_CONCEPT_ID')
    ethnicity_source_value: Optional[str] = Field(..., alias='ETHNICITY_SOURCE_VALUE')
    ethnicity_source_concept_id: Optional[str] = Field(..., alias='ETHNICITY_SOURCE_CONCEPT_ID')

class ObservationPeriod(BaseModel):
    observation_period_id: Optional[int] = Field(..., alias='OBSERVATION_PERIOD_ID')
    person_id: Optional[int] = Field(..., alias='PERSON_ID')
    observation_period_start_date: Optional[datetime] = Field(None, alias='OBSERVATION_PERIOD_START_DATE')
    observation_period_end_date: Optional[datetime] = Field(None, alias='OBSERVATION_PERIOD_END_DATE')
    period_type_concept_id: Optional[int] = Field(..., alias='PERIOD_TYPE_CONCEPT_ID')

class VisitOccurrence(BaseModel):
    visit_occurrence_id: Optional[int] = Field(..., alias='VISIT_OCCURRENCE_ID')
    person_id: Optional[int] = Field(..., alias='PERSON_ID')
    visit_concept_id: Optional[int] = Field(..., alias='VISIT_CONCEPT_ID')
    visit_start_date: Optional[datetime] = Field(None, alias='VISIT_START_DATE')
    visit_start_datetime: Optional[datetime] = Field(None, alias='VISIT_START_DATETIME')
    visit_end_date: Optional[datetime] = Field(None, alias='VISIT_END_DATE')
    visit_end_datetime: Optional[datetime] = Field(None, alias='VISIT_END_DATETIME')
    visit_type_concept_id: Optional[int] = Field(..., alias='VISIT_TYPE_CONCEPT_ID')
    provider_id: Optional[int] = Field(..., alias='PROVIDER_ID')
    care_site_id: Optional[int] = Field(..., alias='CARE_SITE_ID')
    visit_source_value: Optional[str] = Field(..., alias='VISIT_SOURCE_VALUE')
    visit_source_concept_id: Optional[int] = Field(..., alias='VISIT_SOURCE_CONCEPT_ID')
    admitting_source_concept_id: Optional[int] = Field(..., alias='ADMITTING_SOURCE_CONCEPT_ID')
    admitting_source_value: Optional[int] = Field(..., alias='ADMITTING_SOURCE_VALUE')
    discharge_to_concept_id: Optional[int] = Field(..., alias='DISCHARGE_TO_CONCEPT_ID')
    discharge_to_source_value: Optional[int] = Field(..., alias='DISCHARGE_TO_SOURCE_VALUE')
    preceding_visit_occurrence_id: Optional[int] = Field(..., alias='PRECEDING_VISIT_OCCURRENCE_ID')

class VisitDetail(BaseModel):
    visit_detail_id: Optional[int] = Field(None, alias='VISIT_DETAIL_ID')
    person_id: Optional[int] = Field(None, alias='PERSON_ID')
    visit_detail_concept_id: Optional[int] = Field(None, alias='VISIT_DETAIL_CONCEPT_ID')
    visit_detail_start_date: Optional[datetime] = Field(None, alias='VISIT_DETAIL_START_DATE')
    visit_detail_start_datetime: Optional[datetime] = Field(None, alias='VISIT_DETAIL_START_DATETIME')
    visit_detail_end_date: Optional[datetime] = Field(None, alias='VISIT_DETAIL_END_DATE')
    visit_detail_end_datetime: Optional[datetime] = Field(None, alias='VISIT_DETAIL_END_DATETIME')
    visit_detail_type_concept_id: Optional[int] = Field(None, alias='VISIT_DETAIL_TYPE_CONCEPT_ID')
    provider_id: Optional[int] = Field(None, alias='PROVIDER_ID')
    care_site_id: Optional[int] = Field(None, alias='CARE_SITE_ID')
    admitting_source_concept_id: Optional[int] = Field(None, alias='ADMITTING_SOURCE_CONCEPT_ID')
    discharge_to_concept_id: Optional[int] = Field(None, alias='DISCHARGE_TO_CONCEPT_ID')
    preceding_visit_detail_id: Optional[int] = Field(None, alias='PRECEDING_VISIT_DETAIL_ID')
    visit_detail_source_value: Optional[int] = Field(..., alias='VISIT_DETAIL_SOURCE_VALUE')
    visit_detail_source_concept_id: Optional[int] = Field(None, alias='VISIT_DETAIL_SOURCE_CONCEPT_ID')
    admitting_source_value: Optional[int] = Field(..., alias='ADMITTING_SOURCE_VALUE')
    discharge_to_source_value: Optional[int] = Field(..., alias='DISCHARGE_TO_SOURCE_VALUE')
    visit_detail_parent_id: Optional[int] = Field(None, alias='VISIT_DETAIL_PARENT_ID')
    visit_occurrence_id: Optional[int] = Field(None, alias='VISIT_OCCURRENCE_ID')

class ConditionOccurrence(BaseModel):
    condition_occurrence_id: Optional[int] = Field(None, alias='CONDITION_OCCURRENCE_ID')
    person_id: Optional[int] = Field(None, alias='PERSON_ID')
    condition_concept_id: Optional[int] = Field(None, alias='CONDITION_CONCEPT_ID')
    condition_start_date: Optional[datetime] = Field(None, alias='CONDITION_START_DATE')
    condition_start_datetime: Optional[datetime] = Field(None, alias='CONDITION_START_DATETIME')
    condition_end_date: Optional[datetime] = Field(None, alias='CONDITION_END_DATE')
    condition_end_datetime: Optional[datetime] = Field(None, alias='CONDITION_END_DATETIME')
    condition_type_concept_id: Optional[int] = Field(None, alias='CONDITION_TYPE_CONCEPT_ID')
    stop_reason: Optional[str] = Field(..., alias='STOP_REASON')
    provider_id: Optional[int] = Field(None, alias='PROVIDER_ID')
    visit_occurrence_id: Optional[int] = Field(None, alias='VISIT_OCCURRENCE_ID')
    visit_detail_id: Optional[int] = Field(None, alias='VISIT_DETAIL_ID')
    condition_source_value: Optional[str] = Field(..., alias='CONDITION_SOURCE_VALUE')
    condition_source_concept_id: Optional[int] = Field(None, alias='CONDITION_SOURCE_CONCEPT_ID')
    condition_status_source_value: Optional[str] = Field(..., alias='CONDITION_STATUS_SOURCE_VALUE')
    condition_status_concept_id: Optional[int] = Field(None, alias='CONDITION_STATUS_CONCEPT_ID')
    condition_occurrence_id: Optional[int] = Field(None, alias='CONDITION_OCCURRENCE_ID')
    person_id: Optional[int] = Field(None, alias='PERSON_ID')
    condition_concept_id: Optional[int] = Field(None, alias='CONDITION_CONCEPT_ID')
    condition_start_date: Optional[datetime] = Field(None, alias='CONDITION_START_DATE')
    condition_start_datetime: Optional[datetime] = Field(None, alias='CONDITION_START_DATETIME')
    condition_end_date: Optional[datetime] = Field(None, alias='CONDITION_END_DATE')
    condition_end_datetime: Optional[datetime] = Field(None, alias='CONDITION_END_DATETIME')
    condition_type_concept_id: Optional[int] = Field(None, alias='CONDITION_TYPE_CONCEPT_ID')
    stop_reason: Optional[str] = Field(..., alias='STOP_REASON')
    provider_id: Optional[int] = Field(None, alias='PROVIDER_ID')
    visit_occurrence_id: Optional[int] = Field(None, alias='VISIT_OCCURRENCE_ID')
    visit_detail_id: Optional[int] = Field(None, alias='VISIT_DETAIL_ID')
    condition_source_value: Optional[str] = Field(..., alias='CONDITION_SOURCE_VALUE')
    condition_source_concept_id: Optional[int] = Field(None, alias='CONDITION_SOURCE_CONCEPT_ID')
    condition_status_source_value: Optional[str] = Field(..., alias='CONDITION_STATUS_SOURCE_VALUE')
    condition_status_concept_id: Optional[int] = Field(None, alias='CONDITION_STATUS_CONCEPT_ID')

class DrugExposure(BaseModel):
    drug_exposure_id: Optional[int] = Field(None, alias='DRUG_EXPOSURE_ID')
    person_id: Optional[int] = Field(None, alias='PERSON_ID')
    drug_concept_id: Optional[int] = Field(None, alias='DRUG_CONCEPT_ID')
    drug_exposure_start_date: Optional[datetime] = Field(None, alias='DRUG_EXPOSURE_START_DATE')
    drug_exposure_start_datetime: Optional[datetime] = Field(None, alias='DRUG_EXPOSURE_START_DATETIME')
    drug_exposure_end_date: Optional[datetime] = Field(None, alias='DRUG_EXPOSURE_END_DATE')
    drug_exposure_end_datetime: Optional[datetime] = Field(None, alias='DRUG_EXPOSURE_END_DATETIME')
    verbatim_end_date: Optional[datetime] = Field(None, alias='VERBATIM_END_DATE')
    drug_type_concept_id: Optional[int] = Field(None, alias='DRUG_TYPE_CONCEPT_ID')
    stop_reason: Optional[int] = Field(..., alias='STOP_REASON')
    refills: Optional[int] = Field(..., alias='REFILLS')
    quantity: Optional[int] = Field(..., alias='QUANTITY')
    days_supply: Optional[int] = Field(..., alias='DAYS_SUPPLY')
    sig: Optional[int] = Field(..., alias='SIG')
    route_concept_id: Optional[int] = Field(None, alias='ROUTE_CONCEPT_ID')
    lot_number: Optional[str] = Field(..., alias='LOT_NUMBER')
    provider_id: Optional[int] = Field(None, alias='PROVIDER_ID')
    visit_occurrence_id: Optional[int] = Field(None, alias='VISIT_OCCURRENCE_ID')
    visit_detail_id: Optional[int] = Field(None, alias='VISIT_DETAIL_ID')
    drug_source_value: Optional[str] = Field(..., alias='DRUG_SOURCE_VALUE')
    drug_source_concept_id: Optional[int] = Field(None, alias='DRUG_SOURCE_CONCEPT_ID')
    route_source_value: Optional[int] = Field(..., alias='ROUTE_SOURCE_VALUE')
    dose_unit_source_value: Optional[int] = Field(..., alias='DOSE_UNIT_SOURCE_VALUE')

class ProcedureOccurrence(BaseModel):
    procedure_occurrence_id: Optional[int] = Field(None, alias='PROCEDURE_OCCURRENCE_ID')
    person_id: Optional[int] = Field(None, alias='PERSON_ID')
    procedure_concept_id: Optional[int] = Field(None, alias='PROCEDURE_CONCEPT_ID')
    procedure_date: Optional[datetime] = Field(None, alias='PROCEDURE_DATE')
    procedure_datetime: Optional[datetime] = Field(None, alias='PROCEDURE_DATETIME')
    procedure_type_concept_id: Optional[int] = Field(None, alias='PROCEDURE_TYPE_CONCEPT_ID')
    modifier_concept_id: Optional[int] = Field(None, alias='MODIFIER_CONCEPT_ID')
    quantity: Optional[int] = Field(..., alias='QUANTITY')
    provider_id: Optional[int] = Field(None, alias='PROVIDER_ID')
    visit_occurrence_id: Optional[int] = Field(None, alias='VISIT_OCCURRENCE_ID')
    visit_detail_id: Optional[int] = Field(None, alias='VISIT_DETAIL_ID')
    procedure_source_value: Optional[str] = Field(..., alias='PROCEDURE_SOURCE_VALUE')
    procedure_source_concept_id: Optional[int] = Field(None, alias='PROCEDURE_SOURCE_CONCEPT_ID')
    modifier_source_value: Optional[int] = Field(..., alias='MODIFIER_SOURCE_VALUE')

class DeviceExposure(BaseModel):
    device_exposure_id: Optional[int] = Field(None, alias='DEVICE_EXPOSURE_ID')
    person_id: Optional[int] = Field(None, alias='PERSON_ID')
    device_concept_id: Optional[int] = Field(None, alias='DEVICE_CONCEPT_ID')
    device_exposure_start_date: Optional[datetime] = Field(None, alias='DEVICE_EXPOSURE_START_DATE')
    device_exposure_start_datetime: Optional[datetime] = Field(None, alias='DEVICE_EXPOSURE_START_DATETIME')
    device_exposure_end_date: Optional[datetime] = Field(None, alias='DEVICE_EXPOSURE_END_DATE')
    device_exposure_end_datetime: Optional[datetime] = Field(None, alias='DEVICE_EXPOSURE_END_DATETIME')
    device_type_concept_id: Optional[int] = Field(None, alias='DEVICE_TYPE_CONCEPT_ID')
    unique_device_id: Optional[int] = Field(None, alias='UNIQUE_DEVICE_ID')
    quantity: Optional[int] = Field(..., alias='QUANTITY')
    provider_id: Optional[int] = Field(None, alias='PROVIDER_ID')
    visit_occurrence_id: Optional[int] = Field(None, alias='VISIT_OCCURRENCE_ID')
    visit_detail_id: Optional[int] = Field(None, alias='VISIT_DETAIL_ID')
    device_source_value: Optional[int] = Field(..., alias='DEVICE_SOURCE_VALUE')
    device_source_concept_id: Optional[int] = Field(None, alias='DEVICE_SOURCE_CONCEPT_ID')

class Measurement(BaseModel):
    measurement_id: Optional[int] = Field(None, alias='MEASUREMENT_ID')
    person_id: Optional[int] = Field(None, alias='PERSON_ID')
    measurement_concept_id: Optional[int] = Field(None, alias='MEASUREMENT_CONCEPT_ID')
    measurement_date: Optional[datetime] = Field(None, alias='MEASUREMENT_DATE')
    measurement_datetime: Optional[datetime] = Field(None, alias='MEASUREMENT_DATETIME')
    measurement_time: Optional[str] = Field(..., alias='MEASUREMENT_TIME')
    measurement_type_concept_id: Optional[int] = Field(None, alias='MEASUREMENT_TYPE_CONCEPT_ID')
    operator_concept_id: Optional[int] = Field(None, alias='OPERATOR_CONCEPT_ID')
    value_as_number: Optional[int] = Field(..., alias='VALUE_AS_NUMBER')
    value_as_concept_id: Optional[int] = Field(None, alias='VALUE_AS_CONCEPT_ID')
    unit_concept_id: Optional[int] = Field(None, alias='UNIT_CONCEPT_ID')
    range_low: Optional[int] = Field(..., alias='RANGE_LOW')
    range_high: Optional[int] = Field(..., alias='RANGE_HIGH')
    provider_id: Optional[int] = Field(None, alias='PROVIDER_ID')
    visit_occurrence_id: Optional[int] = Field(None, alias='VISIT_OCCURRENCE_ID')
    visit_detail_id: Optional[int] = Field(None, alias='VISIT_DETAIL_ID')
    measurement_source_value: Optional[str] = Field(..., alias='MEASUREMENT_SOURCE_VALUE')
    measurement_source_concept_id: Optional[int] = Field(None, alias='MEASUREMENT_SOURCE_CONCEPT_ID')
    unit_source_value: Optional[int] = Field(..., alias='UNIT_SOURCE_VALUE')
    value_source_value: Optional[int] = Field(..., alias='VALUE_SOURCE_VALUE')

class Observation(BaseModel):
    observation_id: Optional[int] = Field(None, alias='OBSERVATION_ID')
    person_id: Optional[int] = Field(None, alias='PERSON_ID')
    observation_concept_id: Optional[int] = Field(None, alias='OBSERVATION_CONCEPT_ID')
    observation_date: Optional[datetime] = Field(None, alias='OBSERVATION_DATE')
    observation_datetime: Optional[datetime] = Field(None, alias='OBSERVATION_DATETIME')
    observation_type_concept_id: Optional[int] = Field(None, alias='OBSERVATION_TYPE_CONCEPT_ID')
    value_as_number: Optional[int] = Field(..., alias='VALUE_AS_NUMBER')
    value_as_string: Optional[int] = Field(..., alias='VALUE_AS_STRING')
    value_as_concept_id: Optional[int] = Field(None, alias='VALUE_AS_CONCEPT_ID')
    qualifier_concept_id: Optional[int] = Field(None, alias='QUALIFIER_CONCEPT_ID')
    unit_concept_id: Optional[int] = Field(None, alias='UNIT_CONCEPT_ID')
    provider_id: Optional[int] = Field(None, alias='PROVIDER_ID')
    visit_occurrence_id: Optional[int] = Field(None, alias='VISIT_OCCURRENCE_ID')
    visit_detail_id: Optional[int] = Field(None, alias='VISIT_DETAIL_ID')
    observation_source_value: Optional[str] = Field(..., alias='OBSERVATION_SOURCE_VALUE')
    observation_source_concept_id: Optional[int] = Field(None, alias='OBSERVATION_SOURCE_CONCEPT_ID')
    unit_source_value: Optional[int] = Field(..., alias='UNIT_SOURCE_VALUE')
    qualifier_source_value: Optional[int] = Field(..., alias='QUALIFIER_SOURCE_VALUE')

class Death(BaseModel):
    person_id: Optional[int] = Field(None, alias='PERSON_ID')
    death_date: Optional[datetime] = Field(None, alias='DEATH_DATE')
    death_datetime: Optional[datetime] = Field(None, alias='DEATH_DATETIME')
    death_type_concept_id: Optional[int] = Field(None, alias='DEATH_TYPE_CONCEPT_ID')
    cause_concept_id: Optional[int] = Field(None, alias='CAUSE_CONCEPT_ID')
    cause_source_value: Optional[int] = Field(..., alias='CAUSE_SOURCE_VALUE')
    cause_source_concept_id: Optional[int] = Field(None, alias='CAUSE_SOURCE_CONCEPT_ID')

class Note(BaseModel):
    note_id: Optional[int] = Field(None, alias='NOTE_ID')
    person_id: Optional[int] = Field(None, alias='PERSON_ID')
    note_date: Optional[datetime] = Field(None, alias='NOTE_DATE')
    note_datetime: Optional[datetime] = Field(None, alias='NOTE_DATETIME')
    note_type_concept_id: Optional[int] = Field(None, alias='NOTE_TYPE_CONCEPT_ID')
    note_class_concept_id: Optional[int] = Field(None, alias='NOTE_CLASS_CONCEPT_ID')
    note_title: Optional[int] = Field(..., alias='NOTE_TITLE')
    note_text: Optional[int] = Field(..., alias='NOTE_TEXT')
    encoding_concept_id: Optional[int] = Field(None, alias='ENCODING_CONCEPT_ID')
    language_concept_id: Optional[int] = Field(None, alias='LANGUAGE_CONCEPT_ID')
    provider_id: Optional[int] = Field(None, alias='PROVIDER_ID')
    visit_occurrence_id: Optional[int] = Field(None, alias='VISIT_OCCURRENCE_ID')
    visit_detail_id: Optional[int] = Field(None, alias='VISIT_DETAIL_ID')
    note_source_value: Optional[int] = Field(..., alias='NOTE_SOURCE_VALUE')

class NoteNlp(BaseModel):
    note_nlp_id: Optional[int] = Field(None, alias='NOTE_NLP_ID') # A unique identifier for the NLP record. 
    note_id: Optional[int] = Field(None, alias='NOTE_ID') # This is the NOTE_ID for the NOTE record the NLP record is associated to. 
    section_concept_id: Optional[int] = Field(None, alias='SECTION_CONCEPT_ID') # The SECTION_CONCEPT_ID should be used to represent the note section contained in the NOTE_NLP record. These concepts can be found as parts of document panels and are based on the type of note written, i.e. a discharge summary. These panels can be found as concepts with the relationship ‘Subsumes’ to CONCEPT_ID 45875957.
    snippet: Optional[int] = Field(..., alias='SNIPPET')
    offset: Optional[int] = Field(..., alias='OFFSET')
    lexical_variant: Optional[int] = Field(..., alias='LEXICAL_VARIANT')
    note_nlp_concept_id: Optional[int] = Field(None, alias='NOTE_NLP_CONCEPT_ID')
    note_nlp_source_concept_id: Optional[int] = Field(None, alias='NOTE_NLP_SOURCE_CONCEPT_ID')
    nlp_system: Optional[int] = Field(..., alias='NLP_SYSTEM')
    nlp_date: Optional[datetime] = Field(None, alias='NLP_DATE')
    nlp_datetime: Optional[datetime] = Field(None, alias='NLP_DATETIME')
    term_exists: Optional[int] = Field(..., alias='TERM_EXISTS')
    term_temporal: Optional[int] = Field(..., alias='TERM_TEMPORAL')
    term_modifiers: Optional[int] = Field(..., alias='TERM_MODIFIERS')

class Specimen(BaseModel):
    specimen_id: Optional[int] = Field(None, alias='SPECIMEN_ID')
    person_id: Optional[int] = Field(None, alias='PERSON_ID')
    specimen_concept_id: Optional[int] = Field(None, alias='SPECIMEN_CONCEPT_ID')
    specimen_type_concept_id: Optional[int] = Field(None, alias='SPECIMEN_TYPE_CONCEPT_ID')
    specimen_date: Optional[datetime] = Field(None, alias='SPECIMEN_DATE')
    specimen_datetime: Optional[datetime] = Field(None, alias='SPECIMEN_DATETIME')
    quantity: Optional[int] = Field(..., alias='QUANTITY')
    unit_concept_id: Optional[int] = Field(None, alias='UNIT_CONCEPT_ID')
    anatomic_site_concept_id: Optional[int] = Field(None, alias='ANATOMIC_SITE_CONCEPT_ID')
    disease_status_concept_id: Optional[int] = Field(None, alias='DISEASE_STATUS_CONCEPT_ID')
    specimen_source_id: Optional[int] = Field(None, alias='SPECIMEN_SOURCE_ID')
    specimen_source_value: Optional[int] = Field(..., alias='SPECIMEN_SOURCE_VALUE')
    unit_source_value: Optional[int] = Field(..., alias='UNIT_SOURCE_VALUE')
    anatomic_site_source_value: Optional[int] = Field(..., alias='ANATOMIC_SITE_SOURCE_VALUE')
    disease_status_source_value: Optional[int] = Field(..., alias='DISEASE_STATUS_SOURCE_VALUE')

class FactRelationship(BaseModel):
    domain_concept_id_1: Optional[int] = Field(..., alias='DOMAIN_CONCEPT_ID_1')
    fact_id_1: Optional[int] = Field(..., alias='FACT_ID_1')
    domain_concept_id_2: Optional[int] = Field(..., alias='DOMAIN_CONCEPT_ID_2')
    fact_id_2: Optional[int] = Field(..., alias='FACT_ID_2')
    relationship_concept_id: Optional[int] = Field(None, alias='RELATIONSHIP_CONCEPT_ID')

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
