# Test Plan — Restful-Booker API | QA Portfolio

## 1. Objective
Validate the functionality, reliability, and data integrity of the 
Restful-Booker REST API, covering authentication, CRUD operations 
on bookings, and health check endpoints.

## 2. Scope
**Included:**
- Health check endpoint
- Authentication (token generation)
- Booking retrieval (single and all)
- Booking creation
- Full booking update (PUT)
- Partial booking update (PATCH)
- Booking deletion

**Excluded:**
- Filter by name and filter by date (inconsistent behavior — documented as BUG-API-001)
- Performance and load testing
- XML and URL-encoded request formats

## 3. Application Under Test
- **Base URL:** https://restful-booker.herokuapp.com
- **Documentation:** https://restful-booker.herokuapp.com/apidoc/index.html
- **Type:** REST API

## 4. Entry Criteria
- API is accessible and returning responses
- Postman is installed and environment variables are configured
- Valid authentication token has been generated

## 5. Exit Criteria
- All test cases have been executed
- All bugs found have been reported with evidence
- Postman collection has been exported and uploaded to GitHub

## 6. Test Types
- Functional API testing
- Positive and negative test cases
- Data validation via Postman assertions

## 7. Environment
- Tool: Postman
- OS: Windows 10
- Collection format: v2.1

## 8. Identified Risks
- API is public and shared — bookings created by other users may 
  interfere with test execution
- API resets periodically — tokens and booking IDs expire quickly,
  requiring re-authentication before update and delete operations
- Filter endpoints (by name and by date) exhibit inconsistent behavior
  and were excluded from the test suite
