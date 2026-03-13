# ER Diagram – Recommendation System

USERS
- user_id
- name

USER_ACTIVITY
- activity_id
- user_id
- item
- timestamp

RECOMMENDATIONS
- rec_id
- user_id
- item

Relationships

User 1 → N Activity  
User 1 → N Recommendations
