# Test Plan — Cart & Checkout Module | SauceDemo

## 1. Objective
Validate the behavior of the SauceDemo cart and checkout module,
verifying the complete purchase flow under different users and scenarios,
including positive, negative, and special user cases.

## 2. Scope
**Included:**
- Adding products to cart from inventory and individual product page
- Removing products from inventory, individual product page, and cart
- Cart counter
- Checkout form field validations
- Complete purchase flow through order completion

**Excluded:**
- Login module (covered in test-plan-login.md)
- Product sorting and filtering

## 3. Application Under Test
- **URL:** https://www.saucedemo.com
- **Users:**
  - standard_user / secret_sauce (reference for correct behavior)
  - error_user / secret_sauce (special behavior user)

## 4. Entry Criteria
- Successful login with the corresponding user
- Application available and accessible

## 5. Exit Criteria
- All test cases have been executed
- Bugs found have been reported with evidence

## 6. Test Types
- Manual functional testing
- Exploratory testing with special user

## 7. Environment
- Browser: Edge
- OS: Windows 10

## 8. Identified Risks
- error_user behavior is unstable and unpredictable,
  meaning additional bugs may exist beyond those covered in this plan
