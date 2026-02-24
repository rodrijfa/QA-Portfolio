# Test Plan — Login Module | SauceDemo

## 1. Objective
Validate the behavior of the SauceDemo login module under different
authentication scenarios, including positive, negative, and special user cases.

## 2. Scope
**Included:**
- Login form (username, password, login button)
- Error messages
- Successful redirection to inventory
- Special user behavior

**Excluded:**
- Cart, checkout, and inventory modules (covered in separate test plans)

## 3. Application Under Test
- **URL:** https://www.saucedemo.com
- **Available test users:**
  - standard_user / secret_sauce
  - locked_out_user / secret_sauce
  - problem_user / secret_sauce
  - performance_glitch_user / secret_sauce
  - visual_user / secret_sauce

## 4. Entry Criteria
- Application is available and accessible
- Test data is known

## 5. Exit Criteria
- All test cases have been executed
- Bugs found have been reported

## 6. Test Types
- Manual functional testing

## 7. Environment
- Browser: Edge (latest version)
- OS: Windows 10
