## Checklist for filter functionality

### Positive:
+ no filter -> shown all books
- filter by non-existent word(s) -> no results
Filter by book name and by author:
- filter by 1 letter -> filter applied
- filter by more than 1 first  letter -> filter applied
- filter by more than 1 letter in the middle of word -> filter applied
- filter by more than 1 letter in the end of word -> filter applied
- filter by full title -> filter applied
- filter with space -> filter applied
- check that filter is case-insensitive
- check filter returns in initial state pressing x button
- check filter returns in initial state after backspaces
Filter by price:
- filter by 1 number -> filter applied
- filter by part int -> filter applied
- filter by part float -> filter applied
- filter by full price with $ -> filter applied
### Negative:
- enter symbols
- check max length


# TODO:
- allure
- Docker file
- Git
- Git Actions