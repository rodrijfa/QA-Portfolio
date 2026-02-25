# Test Cases — Restful-Booker API

## Module: Health Check

| ID | Title | Method | Endpoint | Request Body | Expected Result | Actual Result | Status |
|----|-------|--------|----------|--------------|----------------|---------------|--------|
| TC-API-001 | Health check returns 201 | GET | /ping | None | Status 201, body "Created" | Status 201, body "Created" | Pass |

## Module: Auth

| ID | Title | Method | Endpoint | Request Body | Expected Result | Actual Result | Status |
|----|-------|--------|----------|--------------|----------------|---------------|--------|
| TC-API-002 | Generate token with valid credentials | POST | /auth | username: admin, password: password123 | Status 200, response contains token string | Status 200, token returned and saved to environment | Pass |
| TC-API-003 | Generate token with invalid credentials | POST | /auth | username: admin, password: wrongpassword | Status 200, response contains "Bad credentials" | Status 200, reason: "Bad credentials" | Pass |

## Module: Get Bookings

| ID | Title | Method | Endpoint | Request Body | Expected Result | Actual Result | Status |
|----|-------|--------|----------|--------------|----------------|---------------|--------|
| TC-API-004 | Get all booking IDs | GET | /booking | None | Status 200, array of bookingid objects | Status 200, array returned, first ID saved to environment | Pass |
| TC-API-005 | Get booking by ID | GET | /booking/:id | None | Status 200, booking object with all required fields | Status 200, all fields present with correct data types | Pass |

## Module: Create Booking

| ID | Title | Method | Endpoint | Request Body | Expected Result | Actual Result | Status |
|----|-------|--------|----------|--------------|----------------|---------------|--------|
| TC-API-006 | Create new booking with valid data | POST | /booking | firstname, lastname, totalprice, depositpaid, bookingdates, additionalneeds | Status 200, response contains bookingid and booking object matching request | Status 200, bookingid returned and saved to environment | Pass |

## Module: Update Booking

| ID | Title | Method | Endpoint | Request Body | Expected Result | Actual Result | Status |
|----|-------|--------|----------|--------------|----------------|---------------|--------|
| TC-API-007 | Full update of existing booking | PUT | /booking/:id | All booking fields with updated values | Status 200, response contains updated booking data | Status 200, all fields updated correctly | Pass |
| TC-API-008 | Partial update of existing booking | PATCH | /booking/:id | Selected fields only (firstname, totalprice) | Status 200, updated fields changed, non-updated fields unchanged | Status 200, updated fields changed, other fields preserved | Pass |

## Module: Delete Booking

| ID | Title | Method | Endpoint | Request Body | Expected Result | Actual Result | Status |
|----|-------|--------|----------|--------------|----------------|---------------|--------|
| TC-API-009 | Delete existing booking | DELETE | /booking/:id | None | Status 201, body "Created" | Status 201, body "Created" | Pass |
