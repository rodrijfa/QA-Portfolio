# Test Cases — Cart & Checkout | SauceDemo

## Module: Cart

| ID | Title | Precondition | Steps | Expected Result | Actual Result | Status |
|----|-------|--------------|-------|----------------|---------------|--------|
| TC-009 | Add product to cart from inventory | Login with standard_user | 1. Click "Add to cart" on any product | Product added, cart counter shows 1 | Product correctly added, cart counter shows 1 | Pass |
| TC-010 | Add all products to cart | Login with standard_user | 1. Click "Add to cart" on all 6 products | Counter shows 6, all products in cart | All products added to cart, counter shows 6 | Pass |
| TC-011 | Remove product from inventory | Login with standard_user | 1. Add product 2. Click "Remove" from inventory | Product removed, counter updates | Product(s) removed, counter updates | Pass |
| TC-012 | Remove product from individual product page | Login with standard_user | 1. Add product 2. Navigate to product page 3. Click "Remove" | Product removed, counter updates | Product correctly removed, counter correctly updated | Pass |
| TC-013 | Remove product from cart | Login with standard_user | 1. Add product 2. Go to cart 3. Click "Remove" | Product removed from cart | Product(s) correctly removed from cart | Pass |
| TC-014 | Add product to cart from inventory with error_user | Login with error_user | 1. Attempt to click "Add to cart" on all 6 products | All products are correctly added | Only items 1, 2 and 5 can be added. Items 3, 4 and 6 do not respond to "Add to cart" click | FAIL |
| TC-015 | Remove product from inventory with error_user | Login with error_user | 1. Add product 2. Click "Remove" from inventory | Product removed, counter updates | Product(s) cannot be removed from inventory | Fail |
| TC-016 | Remove product from individual product page with error_user | Login with error_user | 1. Add product 2. Navigate to product page 3. Click "Remove" | Product removed, counter updates | Product is not removed, counter does not update | FAIL |

## Module: Checkout

| ID | Title | Precondition | Steps | Expected Result | Actual Result | Status |
|----|-------|--------------|-------|----------------|---------------|--------|
| TC-017 | Complete checkout with standard_user | Login with standard_user, at least 1 product in cart | 1. Go to cart 2. Click "Checkout" 3. Fill in First Name, Last Name, Postal Code 4. Click "Continue" 5. Click "Finish" | Purchase completed correctly | Purchase completed correctly, regardless of number of products | Pass |
| TC-018 | Checkout with empty fields | Login with standard_user, at least 1 product in cart | 1. Go to cart 2. Click "Checkout" 3. Leave all fields empty 4. Click "Continue" | Shows error indicating required fields | Shows error: "Error: First Name is required" | Pass |
| TC-019 | Checkout with non-numeric postal code | Login with standard_user, at least 1 product in cart | 1. Fill in First Name and Last Name 2. Enter text in Postal Code 3. Click "Continue" | Shows error indicating Postal Code must be numeric | Purchase completed successfully | FAIL |
| TC-020 | Complete checkout with error_user | Login with error_user, products in cart | 1. Go to cart 2. Click "Checkout" 3. Attempt to fill in all 3 fields 4. Click "Continue" 5. Click "Finish" | Purchase completed correctly | Purchase cannot be completed. "Finish" button is unresponsive | FAIL |
| TC-021 | Last Name field with error_user | Login with error_user | 1. Go to checkout 2. Attempt to type in Last Name field | Field accepts input correctly | No value can be entered in Last Name field, but checkout advances anyway. Purchase cannot be completed | FAIL |
