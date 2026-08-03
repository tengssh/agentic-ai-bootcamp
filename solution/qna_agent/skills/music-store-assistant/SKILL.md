---
name: music-store-assistant
description: "Database schema and query execution for music store data. 
Note: The skill file is located at skills/.../SKILL.md inside this folder. Always run cat on SKILL.md (e.g., cat /path/to/skill/SKILL.md)."
---
# Music Store Schema

## Tables

### Artist
- ArtistId (PRIMARY KEY)
- Name

### Album
- AlbumId (PRIMARY KEY)
- Title
- ArtistId (FOREIGN KEY -> Artist.ArtistId)

### Track
- TrackId (PRIMARY KEY)
- Name
- AlbumId (FOREIGN KEY -> Album.AlbumId)
- MediaTypeId (FOREIGN KEY -> MediaType.MediaTypeId)
- GenreId (FOREIGN KEY -> Genre.GenreId)
- Composer
- Milliseconds
- Bytes
- UnitPrice

### Customer
- CustomerId (PRIMARY KEY)
- FirstName
- LastName
- Company
- Address
- City
- State
- Country
- PostalCode
- Phone
- Fax
- Email
- SupportRepId (FOREIGN KEY -> Employee.EmployeeId)

### Employee
- EmployeeId (PRIMARY KEY)
- LastName
- FirstName
- Title
- ReportsTo (FOREIGN KEY -> Employee.EmployeeId)
- BirthDate
- HireDate
- Address
- City
- State
- Country
- PostalCode
- Phone
- Fax
- Email

### Genre
- GenreId (PRIMARY KEY)
- Name

### MediaType
- MediaTypeId (PRIMARY KEY)
- Name

### Invoice
- InvoiceId (PRIMARY KEY)
- CustomerId (FOREIGN KEY -> Customer.CustomerId)
- InvoiceDate
- BillingAddress
- BillingCity
- BillingState
- BillingCountry
- BillingPostalCode
- Total

### InvoiceLine
- InvoiceLineId (PRIMARY KEY)
- InvoiceId (FOREIGN KEY -> Invoice.InvoiceId)
- TrackId (FOREIGN KEY -> Track.TrackId)
- UnitPrice
- Quantity

## Example Query

-- Get all artists with more than 1 album
SELECT ArtistId, Name, COUNT(*) AS total_albums
FROM Artist
JOIN Album USING (ArtistId)
GROUP BY ArtistId, Name
HAVING total_albums > 1
ORDER BY total_albums DESC;
