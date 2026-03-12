# Django Model Fields and ORM Cheat Sheet

## 1. Django Model Field Types

Django fields map Python data types to database column types.

### String Fields

  Field        Use Case
  ------------ -----------------------------------
  CharField    Short text (names, titles)
  TextField    Long text (descriptions, content)
  SlugField    SEO-friendly URL strings
  EmailField   Email addresses with validation
  URLField     Website URLs
  UUIDField    Universally unique identifiers

Example:

``` python
name = models.CharField(max_length=200)
description = models.TextField()
email = models.EmailField()
```

------------------------------------------------------------------------

### Numeric Fields

  Field                  Use Case
  ---------------------- -------------------------
  IntegerField           Whole numbers
  BigIntegerField        Large integers
  FloatField             Floating point numbers
  DecimalField           Precise numbers (money)
  PositiveIntegerField   Positive numbers only

Example:

``` python
price = models.DecimalField(max_digits=10, decimal_places=2)
stock = models.IntegerField()
rating = models.FloatField()
```

------------------------------------------------------------------------

### Boolean Fields

  Field          Use Case
  -------------- ---------------------
  BooleanField   True / False values

Example:

``` python
is_active = models.BooleanField(default=True)
```

------------------------------------------------------------------------

### Date and Time Fields

  Field           Use Case
  --------------- ----------------------
  DateField       Stores a date
  TimeField       Stores time
  DateTimeField   Stores date and time
  DurationField   Time duration

Example:

``` python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

------------------------------------------------------------------------

### File Fields

  Field        Use Case
  ------------ ---------------
  FileField    File uploads
  ImageField   Image uploads

Example:

``` python
image = models.ImageField(upload_to="products/")
```

------------------------------------------------------------------------

### JSON and Special Fields

  Field         Use Case
  ------------- --------------------
  JSONField     Store JSON data
  BinaryField   Store binary data
  UUIDField     Unique identifiers

Example:

``` python
metadata = models.JSONField()
```

------------------------------------------------------------------------

### Relationship Fields

  Field             Relationship
  ----------------- --------------
  ForeignKey        One-to-many
  ManyToManyField   Many-to-many
  OneToOneField     One-to-one

Example:

``` python
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
```

------------------------------------------------------------------------

### Auto Fields

  Field          Description
  -------------- -------------------------
  AutoField      Auto increment ID
  BigAutoField   Large auto increment ID

------------------------------------------------------------------------

### Most Common Fields in Real Projects

    CharField
    TextField
    IntegerField
    DecimalField
    BooleanField
    DateTimeField
    ForeignKey
    JSONField
    ImageField

------------------------------------------------------------------------

# 2. Django ORM Cheat Sheet

ORM (Object Relational Mapper) allows interaction with the database
using Python instead of SQL.

------------------------------------------------------------------------

## Basic Queries

  ORM          Description
  ------------ ---------------------
  .all()       Get all records
  .get()       Get a single record
  .filter()    Filter records
  .exclude()   Exclude records

Example:

``` python
Product.objects.all()
Product.objects.get(id=1)
Product.objects.filter(price__gt=1000)
```

------------------------------------------------------------------------

## Create, Update, Delete

  ORM         Purpose
  ----------- -------------------
  .create()   Create new record
  .save()     Save object
  .update()   Update records
  .delete()   Delete records

Example:

``` python
Product.objects.create(name="Laptop", price=50000)

Product.objects.filter(id=1).update(price=60000)

Product.objects.filter(id=1).delete()
```

------------------------------------------------------------------------

## Query Modifiers

  ORM           Purpose
  ------------- ------------------------
  .order_by()   Sort records
  .count()      Count records
  .exists()     Check if record exists
  .first()      First record
  .last()       Last record

Example:

``` python
Product.objects.order_by("-price")
Product.objects.count()
Product.objects.first()
```

------------------------------------------------------------------------

## Search and Filtering

  Lookup          Purpose
  --------------- -------------------------
  \_\_contains    Case-sensitive search
  \_\_icontains   Case-insensitive search
  \_\_gt          Greater than
  \_\_lt          Less than
  \_\_gte         Greater than or equal
  \_\_lte         Less than or equal

Example:

``` python
Product.objects.filter(name__icontains="phone")
Product.objects.filter(price__gt=10000)
```

------------------------------------------------------------------------

## Aggregations

  Function   Purpose
  ---------- ---------------
  Avg()      Average
  Max()      Maximum
  Min()      Minimum
  Sum()      Total
  Count()    Count records

Example:

``` python
from django.db.models import Avg
Product.objects.aggregate(Avg("price"))
```

------------------------------------------------------------------------

## Query Optimization

  Method               Purpose
  -------------------- -------------------------------
  select_related()     Optimize foreign key queries
  prefetch_related()   Optimize many-to-many queries

Example:

``` python
Order.objects.select_related("user")
```

------------------------------------------------------------------------

## Field Selection

  Method          Purpose
  --------------- ---------------------------
  values()        Return dictionaries
  values_list()   Return lists
  only()          Load only specific fields
  defer()         Skip certain fields

Example:

``` python
Product.objects.values("name", "price")
```

------------------------------------------------------------------------

## Limiting Results

Example:

``` python
Product.objects.all()[:5]
```

Equivalent SQL:

``` sql
LIMIT 5
```

------------------------------------------------------------------------

## OR Queries with Q Objects

``` python
from django.db.models import Q

Product.objects.filter(
    Q(price__gt=50000) | Q(stock__gt=10)
)
```

------------------------------------------------------------------------

## Most Important ORM Methods

    .objects.all()
    .objects.get()
    .objects.filter()
    .objects.create()
    .objects.update()
    .objects.delete()
    .objects.count()
    .objects.order_by()
    .objects.exists()
