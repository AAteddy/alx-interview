# UTF-8 Validation

### Intuition

To resolve whether the data sequence is a valid UTF-8 encoding, one needs to examine each integer and identify the number of bytes the current character should have. This is done by checking the most significant bits (MSB) of each integer:

- If an integer starts with 0, it should be a single byte character.
- Otherwise, count the number of consecutive 1 bits at the start to know how many bytes the character should have. The count must be at least 2, and no more than 4, as UTF-8 can't have more than 4 byte characters.
