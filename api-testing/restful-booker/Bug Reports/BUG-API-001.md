# BUG-API-001 — Filter by Name and Filter by Date Return Inconsistent Results

## General Information
| Field | Detail |
|-------|--------|
| ID | BUG-API-001 |
| Date | 2026-02-25 |
| Reported by | Rodrigo Flores Agreda |
| Severity | Medium |
| Priority | Medium |
| Status | Open |
| Related TC | N/A — excluded from test suite due to inconsistent behavior |

## Description
The GetBookingIds endpoint supports optional query parameters to filter 
results by firstname/lastname and by checkin/checkout date. Both filter 
variants exhibit inconsistent and unreliable behavior, returning different 
results across executions with identical parameters.

## Steps to Reproduce
**Filter by name:**
1. Execute GET /booking?firstname=John&lastname=Smith
2. Observe response
3. Execute the same request again
4. Compare results

**Filter by date:**
1. Execute GET /booking?checkin=2018-01-01&checkout=2019-01-01
2. Observe response
3. Execute the same request again
4. Compare results

## Expected Result
Both filter variants should return a consistent, deterministic subset 
of booking IDs matching the specified criteria across all executions.

## Actual Result
Filter by name returned an empty array `[]` on initial executions, 
then returned a large subset of bookings (~700 results) on subsequent 
executions with the same parameters, suggesting non-deterministic 
filtering logic.

Filter by date alternated between returning an empty array and a 
400 Bad Request response across executions with identical parameters.

## Impact
Filtering functionality cannot be relied upon for production use cases 
that require deterministic search results, such as booking lookups by 
guest name or date range.

## Environment
| Field | Detail |
|-------|--------|
| Tool | Postman |
| OS | Windows 10 |
| Base URL | https://restful-booker.herokuapp.com |

## Note
These endpoints were excluded from the test suite due to their 
inconsistent behavior. The root cause may be related to the shared 
and periodically reset nature of this public test API rather than 
a production defect.
