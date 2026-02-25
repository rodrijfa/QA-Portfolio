# API Testing — Restful-Booker | QA Portfolio

API testing project over the Restful-Booker REST API 
(https://restful-booker.herokuapp.com), covering authentication, 
full CRUD operations on bookings, and health check validation.

## Repository Structure
- `test-plan/` — Test plan covering scope, risks and approach
- `test-cases/` — Executed test cases with results
- `bug-reports/` — Bugs found during execution
- `collections/` — Exportable Postman collection (v2.1)

## Coverage Summary
| Module | Test Cases | Result |
|--------|-----------|--------|
| Health Check | 1 | ✅ Pass |
| Auth | 2 | ✅ Pass |
| Get Bookings | 2 | ✅ Pass |
| Create Booking | 1 | ✅ Pass |
| Update Booking | 2 | ✅ Pass |
| Delete Booking | 1 | ✅ Pass |
| **Total** | **9** | **9/9 Pass** |

## Bugs Found
| ID | Title | Severity |
|----|-------|----------|
| BUG-API-001 | Filter by Name and Filter by Date return inconsistent results | Medium |

## Tools Used
- Postman — Request execution and assertions
- GitHub — Version control and documentation
- Markdown — Documentation

## How to Use the Collection
1. Download `collections/restful-booker.postman_collection.json`
2. Open Postman and click **Import**
3. Create an environment with variable `base_url` set to `https://restful-booker.herokuapp.com`
4. Run **02 - Auth → Create Token** first to generate a valid token
5. Execute requests in order from 01 to 07

## Author
Rodrigo Flores Agreda
[LinkedIn](https://www.linkedin.com/in/rodrigo-flores-agreda/) | 
[GitHub](https://github.com/rodrijfa)
