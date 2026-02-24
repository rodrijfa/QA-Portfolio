# Test Cases — Login | SauceDemo

| ID | Title | Precondition | Steps | Expected Result | Actual Result | Status |
|----|-------|--------------|-------|----------------|---------------|--------|
| TC-001 | Successful login with standard user | App open | 1. Enter "standard_user" in username 2. Enter "secret_sauce" in password 3. Click "Login" | Redirects to /inventory.html | Correctly redirects to /inventory.html and displays product catalog | Pass |
| TC-002 | Login with locked out user | App open | 1. Enter "locked_out_user" 2. Enter "secret_sauce" 3. Click "Login" | Shows error: "Epic sadface: Sorry, this user has been locked out." | Shows message: "Epic sadface: Sorry, this user has been locked out." | Pass |
| TC-003 | Login with incorrect password | App open | 1. Enter "standard_user" 2. Enter "wrongpass" 3. Click "Login" | Shows invalid credentials error | Shows message: "Epic sadface: Username and password do not match any user in this service" | Pass |
| TC-004 | Login with empty fields | App open | 1. Enter nothing 2. Click "Login" | Shows error indicating username is required | Shows message: "Epic sadface: Username is required" | Pass |
| TC-005 | Login with username only, no password | App open | 1. Enter "standard_user" 2. Leave password empty 3. Click "Login" | Shows error indicating password is required | Shows message: "Epic sadface: Password is required" | Pass |
| TC-006 | Login with performance_glitch_user | App open | 1. Enter "performance_glitch_user" 2. Enter "secret_sauce" 3. Click "Login" | Successful login in reasonable time with visual feedback during load | Login successful, but a delay of approximately 3-5 seconds observed before redirecting to /inventory.html. Button shows no visual feedback during wait. | Pass |
| TC-007 | Login with special characters in username | App open | 1. Enter "!@#$%^&*()" in username 2. Enter "secret_sauce" 3. Click "Login" | Shows invalid credentials error | Shows message: "Epic sadface: Username and password do not match any user in this service" | Pass |
| TC-008 | Login with visual_user | App open | 1. Enter "visual_user" in username 2. Enter "secret_sauce" 3. Click "Login" | Successful login. Product images in inventory are correct and correspond to each item. | "Sauce Labs Backpack" item displays incorrect image | FAIL |
