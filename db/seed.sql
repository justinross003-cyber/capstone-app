
INSERT INTO Customers (CustomerId, Name, Email, CreatedAt) VALUES
    ('11111111-1111-1111-1111-111111111111', 'Alice Inwonderland', 'alice@wonderland.com', '2025-10-14T12:00:00Z'),
    ('22222222-2222-2222-2222-222222222222', 'Johnny Silverhand', 'johnny@samurai.io', '2025-10-14T12:10:00Z'),
    ('33333333-3333-3333-3333-333333333333', 'Aragon Sonofarathorn', 'aragorn@gondor.gov', '2025-10-14T12:20:00Z');

INSERT INTO Orders (OrderId, CustomerId, Total, CreatedAt) VALUES
    ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa', '11111111-1111-1111-1111-111111111111', 49.99, '2025-10-14T12:30:00Z'),
    ('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb', '22222222-2222-2222-2222-222222222222', 19.50, '2025-10-14T12:31:00Z'),
    ('cccccccc-cccc-cccc-cccc-cccccccccccc', '11111111-1111-1111-1111-111111111111', 5.00,  '2025-10-14T12:32:00Z'),
    ('dddddddd-dddd-dddd-dddd-dddddddddddd', '33333333-3333-3333-3333-333333333333', 120.00,'2025-10-14T12:33:00Z');
