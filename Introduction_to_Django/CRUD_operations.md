
#### **CRUD_operations.md**
Include all four operations combined with clear explanations.

---

## ⚙️ TASK 2 — Django Admin Interface
### 🎯 Objective:
Enable model management through the Django Admin and customize its appearance.

### 🪜 Steps:

#### 1. Register model
In `bookshelf/admin.py`:
```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')
