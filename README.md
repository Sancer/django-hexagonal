# Django Hexagonal Example

### Context approach
 - Catalog 
   -  Contains the products and the logics related to variants 
 - Purchase
   - Contains logic related to prices, offers and shopping cart 
 - Logistic
   - Contains the shipping, stock and destination warehouse logics.


### TODO
- [x] Change pk|id from integer autoincremental to uuid4
- [x] Create first django app | context
- [x] Create Shared context
- [ ] Create basic Value Objects
- [ ] Create base Use Case
- [ ] Create domain Repository
- [ ] Create basic repository implementation in Django
- [ ] Make a first use case