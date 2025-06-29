# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T18:03:44+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, constr


class BadRequest(BaseModel):
    message: Optional[str] = None


class Credentials(BaseModel):
    district_username: Optional[str] = None


class District(BaseModel):
    id: Optional[str] = None
    mdr_number: Optional[str] = None
    name: Optional[str] = None


class DistrictResponse(BaseModel):
    data: Optional[District] = None


class State(Enum):
    running = 'running'
    pending = 'pending'
    error = 'error'
    paused = 'paused'


class DistrictStatus(BaseModel):
    error: Optional[str] = None
    id: Optional[str] = None
    instant_login: Optional[bool] = None
    last_sync: Optional[str] = None
    launch_date: Optional[str] = None
    pause_end: Optional[str] = None
    pause_start: Optional[str] = None
    sis_type: Optional[str] = None
    state: Optional[State] = None


class DistrictStatusResponse(BaseModel):
    data: Optional[DistrictStatus] = None


class DistrictStatusResponses(BaseModel):
    data: Optional[List[DistrictStatusResponse]] = None


class DistrictsResponse(BaseModel):
    data: Optional[List[DistrictResponse]] = None


class GradeLevelsResponse(BaseModel):
    data: Optional[List[str]] = None


class InternalError(BaseModel):
    message: Optional[str] = None


class Location(BaseModel):
    address: Optional[str] = None
    city: Optional[str] = None
    lat: Optional[str] = None
    lon: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[str] = None


class Name(BaseModel):
    first: Optional[str] = None
    last: Optional[str] = None
    middle: Optional[str] = None


class NotFound(BaseModel):
    message: Optional[str] = None


class Principal(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None


class HighGrade(Enum):
    field_1 = '1'
    field_2 = '2'
    field_3 = '3'
    field_4 = '4'
    field_5 = '5'
    field_6 = '6'
    field_7 = '7'
    field_8 = '8'
    field_9 = '9'
    field_10 = '10'
    field_11 = '11'
    field_12 = '12'
    PreKindergarten = 'PreKindergarten'
    Kindergarten = 'Kindergarten'
    PostGraduate = 'PostGraduate'
    Other = 'Other'


class LowGrade(Enum):
    field_1 = '1'
    field_2 = '2'
    field_3 = '3'
    field_4 = '4'
    field_5 = '5'
    field_6 = '6'
    field_7 = '7'
    field_8 = '8'
    field_9 = '9'
    field_10 = '10'
    field_11 = '11'
    field_12 = '12'
    PreKindergarten = 'PreKindergarten'
    Kindergarten = 'Kindergarten'
    PostGraduate = 'PostGraduate'
    Other = 'Other'


class School(BaseModel):
    created: Optional[str] = None
    district: Optional[str] = None
    high_grade: Optional[HighGrade] = None
    id: Optional[str] = None
    last_modified: Optional[str] = None
    location: Optional[Location] = None
    low_grade: Optional[LowGrade] = None
    mdr_number: Optional[str] = None
    name: Optional[str] = None
    nces_id: Optional[str] = None
    phone: Optional[str] = None
    principal: Optional[Principal] = None
    school_number: Optional[str] = None
    sis_id: Optional[str] = None
    state_id: Optional[str] = None


class SchoolAdmin(BaseModel):
    credentials: Optional[Credentials] = None
    district: Optional[str] = None
    email: Optional[str] = None
    id: Optional[str] = None
    name: Optional[Name] = None
    schools: Optional[List[str]] = None
    staff_id: Optional[str] = None
    title: Optional[str] = None


class SchoolAdminResponse(BaseModel):
    data: Optional[SchoolAdmin] = None


class SchoolAdminsResponse(BaseModel):
    data: Optional[List[SchoolAdminResponse]] = None


class SchoolResponse(BaseModel):
    data: Optional[School] = None


class SchoolsResponse(BaseModel):
    data: Optional[List[SchoolResponse]] = None


class Grade(Enum):
    field_1 = '1'
    field_2 = '2'
    field_3 = '3'
    field_4 = '4'
    field_5 = '5'
    field_6 = '6'
    field_7 = '7'
    field_8 = '8'
    field_9 = '9'
    field_10 = '10'
    field_11 = '11'
    field_12 = '12'
    PreKindergarten = 'PreKindergarten'
    Kindergarten = 'Kindergarten'
    PostGraduate = 'PostGraduate'
    Other = 'Other'


class Subject(Enum):
    english_language_arts = 'english/language arts'
    math = 'math'
    science = 'science'
    social_studies = 'social studies'
    language = 'language'
    homeroom_advisory = 'homeroom/advisory'
    interventions_online_learning = 'interventions/online learning'
    technology_and_engineering = 'technology and engineering'
    PE_and_health = 'PE and health'
    arts_and_music = 'arts and music'
    other = 'other'


class EllStatus(Enum):
    Y = 'Y'
    N = 'N'
    field_ = ''


class Gender(Enum):
    M = 'M'
    F = 'F'
    field_ = ''


class HispanicEthnicity(Enum):
    Y = 'Y'
    N = 'N'
    field_ = ''


class Race(Enum):
    Caucasian = 'Caucasian'
    Asian = 'Asian'
    Black_or_African_American = 'Black or African American'
    American_Indian = 'American Indian'
    Hawaiian_or_Other_Pacific_Islander = 'Hawaiian or Other Pacific Islander'
    Two_or_More_Races = 'Two or More Races'
    Unknown = 'Unknown'
    field_ = ''


class Student(BaseModel):
    created: Optional[str] = None
    credentials: Optional[Credentials] = None
    district: Optional[str] = None
    dob: Optional[constr(pattern=r'(?:[0-9]{1,2})/([0-9]{1,2})/([0-9]{4})')] = None
    ell_status: Optional[EllStatus] = None
    email: Optional[str] = None
    gender: Optional[Gender] = None
    grade: Optional[Grade] = None
    graduation_year: Optional[str] = None
    hispanic_ethnicity: Optional[HispanicEthnicity] = None
    id: Optional[str] = None
    last_modified: Optional[str] = None
    location: Optional[Location] = None
    name: Optional[Name] = None
    race: Optional[Race] = None
    school: Optional[str] = None
    schools: Optional[List[str]] = None
    sis_id: Optional[str] = None
    state_id: Optional[str] = None
    student_number: Optional[str] = None


class StudentContact(BaseModel):
    district: Optional[str] = None
    email: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    phone_type: Optional[str] = None
    relationship: Optional[str] = None
    sis_id: Optional[str] = None
    student: Optional[str] = None
    type: Optional[str] = None


class StudentContactResponse(BaseModel):
    data: Optional[StudentContact] = None


class StudentContactsForStudentResponse(BaseModel):
    data: Optional[List[StudentContact]] = None


class StudentContactsResponse(BaseModel):
    data: Optional[List[StudentContactResponse]] = None


class StudentResponse(BaseModel):
    data: Optional[Student] = None


class StudentsResponse(BaseModel):
    data: Optional[List[StudentResponse]] = None


class Teacher(BaseModel):
    created: Optional[str] = None
    credentials: Optional[Credentials] = None
    district: Optional[str] = None
    email: Optional[str] = None
    id: Optional[str] = None
    last_modified: Optional[str] = None
    name: Optional[Name] = None
    school: Optional[str] = None
    schools: Optional[List[str]] = None
    sis_id: Optional[str] = None
    state_id: Optional[str] = None
    teacher_number: Optional[str] = None
    title: Optional[str] = None


class TeacherResponse(BaseModel):
    data: Optional[Teacher] = None


class TeachersResponse(BaseModel):
    data: Optional[List[TeacherResponse]] = None


class Term(BaseModel):
    end_date: Optional[str] = None
    name: Optional[str] = None
    start_date: Optional[str] = None


class DistrictAdmin(BaseModel):
    district: Optional[str] = None
    email: Optional[str] = None
    id: Optional[str] = None
    name: Optional[Name] = None
    title: Optional[str] = None


class DistrictAdminResponse(BaseModel):
    data: Optional[DistrictAdmin] = None


class DistrictAdminsResponse(BaseModel):
    data: Optional[List[DistrictAdmin]] = None


class Section(BaseModel):
    course_description: Optional[str] = None
    course_name: Optional[str] = None
    course_number: Optional[str] = None
    created: Optional[str] = None
    district: Optional[str] = None
    grade: Optional[Grade] = None
    id: Optional[str] = None
    last_modified: Optional[str] = None
    name: Optional[str] = None
    period: Optional[str] = None
    school: Optional[str] = None
    section_number: Optional[str] = None
    sis_id: Optional[str] = None
    students: Optional[List[str]] = None
    subject: Optional[Subject] = None
    teacher: Optional[str] = None
    teachers: Optional[List[str]] = None
    term: Optional[Term] = None


class SectionResponse(BaseModel):
    data: Optional[Section] = None


class SectionsResponse(BaseModel):
    data: Optional[List[SectionResponse]] = None
