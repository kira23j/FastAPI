from datetime import datetime
from sqlalchemy import Column ,DataTime
from sqlalchemy.orm import declarative_mixin

@declarative_mixin
class Timestamp:
    created_at=Column(DataTime,default=datetime.utcnow,nullable=False)
    updated_at=Column(DataTime,default=datetime.utcnow,nullable=False)