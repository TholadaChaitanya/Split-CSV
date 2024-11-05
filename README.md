# Split CSV File on Condition

A simple Python script to split a large CSV file into smaller parts if it exceeds a specified size limit (default: 50 MB). Each split file includes the header from the original CSV to keep data structure consistent.

- **Conditional Splitting**: Only splits the file if it’s larger than the specified size.
- **Header Retention**: Each split file includes the original CSV's header.
- **Easy Identification**: Automatically names part files with numbered suffixes.
