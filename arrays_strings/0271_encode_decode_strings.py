"""
271. Encode and Decode Strings
Difficulty: Medium

Design an algorithm to encode a list of strings to a string. The encoded string is then sent 
over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}

Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  // ... your code
  return strs;
}

So Machine 1 does:
string encoded_string = encode(strs);
and Machine 2 does:
vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).

Example 1:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
msg = "5#Hello5#World"

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
strs = ["Hello","World"]

Example 2:
Input: dummy_input = [""]
Output: [""]

Constraints:
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] contains any possible characters out of 256 valid ascii characters.

Notes:
- Key challenge: Need a way to delimit strings without ambiguity
- The strings can contain any ASCII character, including the delimiter itself
- Common approaches:
  1. Length prefix + delimiter: "length#string" format (current solution)
  2. Escape sequences: Escape special characters
  3. Different delimiters: Use less common characters
  4. Base64 encoding: Encode each string separately
  5. JSON encoding: Use JSON serialization (but problem says no serialize methods)
- Time complexity: O(n) where n is total length of all strings
- Space complexity: O(n) for the encoded string
- Edge cases: Empty strings, strings containing '#', very long strings, special characters
"""

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Approach 1: Length Prefix with Delimiter (Current)
        Time Complexity: O(n) where n is total length of all strings
        Space Complexity: O(n) for encoded string
        
        Encode each string as "length#string" format.
        The length tells us exactly how many characters to read after the '#'.
        This handles any character including '#' in the strings themselves.
        """
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + '#' + s)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        """
        Decode the encoded string back to list of strings.
        Time Complexity: O(n) where n is length of encoded string
        Space Complexity: O(n) for decoded list
        """
        decoded = []
        i = 0
        while i < len(s):
            delimiter_pos = s.find('#', i)
            length = int(s[i:delimiter_pos])
            start = delimiter_pos + 1
            decoded.append(s[start:start + length])
            i = start + length
        return decoded


class CodecEscape:
    """
    Approach 2: Escape Sequence Method
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Use escape sequences to handle delimiter characters in strings.
    Escape '#' as '##' and use a different delimiter like '|' or escape '#' itself.
    """
    def encode(self, strs: List[str]) -> str:
        """Encode using escape sequences: escape '#' as '##'"""
        encoded = []
        for s in strs:
            # Escape '#' by doubling it
            escaped = s.replace('#', '##')
            encoded.append(str(len(escaped)) + '#' + escaped)
        return ''.join(encoded)
    
    def decode(self, s: str) -> List[str]:
        """Decode by reading length, then unescaping"""
        decoded = []
        i = 0
        while i < len(s):
            delimiter_pos = s.find('#', i)
            length = int(s[i:delimiter_pos])
            start = delimiter_pos + 1
            escaped_str = s[start:start + length]
            # Unescape: '##' -> '#'
            decoded.append(escaped_str.replace('##', '#'))
            i = start + length
        return decoded


class CodecDelimiter:
    """
    Approach 3: Using Different Delimiter
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Use a less common delimiter like '|' or a multi-character delimiter.
    Still need length prefix to handle delimiter in strings.
    """
    DELIMITER = '|'
    
    def encode(self, strs: List[str]) -> str:
        """Encode using a different delimiter"""
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + self.DELIMITER + s)
        return ''.join(encoded)
    
    def decode(self, s: str) -> List[str]:
        """Decode using the custom delimiter"""
        decoded = []
        i = 0
        while i < len(s):
            delimiter_pos = s.find(self.DELIMITER, i)
            length = int(s[i:delimiter_pos])
            start = delimiter_pos + 1
            decoded.append(s[start:start + length])
            i = start + length
        return decoded


class CodecChunkSize:
    """
    Approach 4: Fixed Chunk Size with Padding
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Use fixed-width length prefix (e.g., 4 digits) to avoid parsing issues.
    This makes decoding slightly more efficient.
    """
    CHUNK_SIZE = 4  # Fixed width for length
    
    def encode(self, strs: List[str]) -> str:
        """Encode with fixed-width length prefix"""
        encoded = []
        for s in strs:
            # Pad length to fixed width
            length_str = str(len(s)).zfill(self.CHUNK_SIZE)
            encoded.append(length_str + '#' + s)
        return ''.join(encoded)
    
    def decode(self, s: str) -> List[str]:
        """Decode with fixed-width length prefix"""
        decoded = []
        i = 0
        while i < len(s):
            # Read fixed-width length
            length = int(s[i:i + self.CHUNK_SIZE])
            delimiter_pos = i + self.CHUNK_SIZE
            start = delimiter_pos + 1
            decoded.append(s[start:start + length])
            i = start + length
        return decoded


def test_solution():
    """Test cases for encode/decode solutions"""
    
    # Test case 1: Basic example
    print("Test 1: Basic example - ['Hello', 'World']")
    codec = Codec()
    strs1 = ["Hello", "World"]
    encoded1 = codec.encode(strs1)
    decoded1 = codec.decode(encoded1)
    assert decoded1 == strs1, f"Test 1 failed: expected {strs1}, got {decoded1}"
    print(f"  Encoded: {encoded1}")
    print(f"  Decoded: {decoded1} ✓")
    
    # Test case 2: Empty strings
    print("\nTest 2: Empty strings - ['', '']")
    strs2 = ["", ""]
    encoded2 = codec.encode(strs2)
    decoded2 = codec.decode(encoded2)
    assert decoded2 == strs2, f"Test 2 failed: expected {strs2}, got {decoded2}"
    print(f"  Encoded: {encoded2}")
    print(f"  Decoded: {decoded2} ✓")
    
    # Test case 3: Single empty string
    print("\nTest 3: Single empty string - ['']")
    strs3 = [""]
    encoded3 = codec.encode(strs3)
    decoded3 = codec.decode(encoded3)
    assert decoded3 == strs3, f"Test 3 failed: expected {strs3}, got {decoded3}"
    print(f"  Encoded: {encoded3}")
    print(f"  Decoded: {decoded3} ✓")
    
    # Test case 4: Strings containing '#'
    print("\nTest 4: Strings containing '#' - ['Hello#World', 'Test#']")
    strs4 = ["Hello#World", "Test#"]
    encoded4 = codec.encode(strs4)
    decoded4 = codec.decode(encoded4)
    assert decoded4 == strs4, f"Test 4 failed: expected {strs4}, got {decoded4}"
    print(f"  Encoded: {encoded4}")
    print(f"  Decoded: {decoded4} ✓")
    
    # Test case 5: Special characters
    print("\nTest 5: Special characters - ['Hello\nWorld', 'Tab\tHere']")
    strs5 = ["Hello\nWorld", "Tab\tHere"]
    encoded5 = codec.encode(strs5)
    decoded5 = codec.decode(encoded5)
    assert decoded5 == strs5, f"Test 5 failed: expected {strs5}, got {decoded5}"
    print(f"  Encoded: {encoded5}")
    print(f"  Decoded: {decoded5} ✓")
    
    # Test case 6: Numbers in strings
    print("\nTest 6: Numbers in strings - ['123', '456']")
    strs6 = ["123", "456"]
    encoded6 = codec.encode(strs6)
    decoded6 = codec.decode(encoded6)
    assert decoded6 == strs6, f"Test 6 failed: expected {strs6}, got {decoded6}"
    print(f"  Encoded: {encoded6}")
    print(f"  Decoded: {decoded6} ✓")
    
    # Test case 7: Long strings
    print("\nTest 7: Long strings")
    strs7 = ["a" * 100, "b" * 200]
    encoded7 = codec.encode(strs7)
    decoded7 = codec.decode(encoded7)
    assert decoded7 == strs7, f"Test 7 failed: expected {strs7}, got {decoded7}"
    print(f"  Encoded length: {len(encoded7)}")
    print(f"  Decoded: {decoded7} ✓")
    
    # Test case 8: Mixed content
    print("\nTest 8: Mixed content - ['Hello', '', 'World#123', '']")
    strs8 = ["Hello", "", "World#123", ""]
    encoded8 = codec.encode(strs8)
    decoded8 = codec.decode(encoded8)
    assert decoded8 == strs8, f"Test 8 failed: expected {strs8}, got {decoded8}"
    print(f"  Encoded: {encoded8}")
    print(f"  Decoded: {decoded8} ✓")
    
    # Test case 9: Single character strings
    print("\nTest 9: Single character strings - ['a', 'b', 'c']")
    strs9 = ["a", "b", "c"]
    encoded9 = codec.encode(strs9)
    decoded9 = codec.decode(encoded9)
    assert decoded9 == strs9, f"Test 9 failed: expected {strs9}, got {decoded9}"
    print(f"  Encoded: {encoded9}")
    print(f"  Decoded: {decoded9} ✓")
    
    # Test case 10: Unicode characters (if supported)
    print("\nTest 10: Unicode characters - ['Hello', '世界']")
    strs10 = ["Hello", "世界"]
    encoded10 = codec.encode(strs10)
    decoded10 = codec.decode(encoded10)
    assert decoded10 == strs10, f"Test 10 failed: expected {strs10}, got {decoded10}"
    print(f"  Encoded: {encoded10}")
    print(f"  Decoded: {decoded10} ✓")
    
    # Test case 11: Compare all approaches
    print("\nTest 11: Comparing all approaches")
    test_cases = [
        ["Hello", "World"],
        ["", ""],
        [""],
        ["Hello#World", "Test#"],
        ["Hello\nWorld", "Tab\tHere"],
        ["123", "456"],
        ["a" * 100, "b" * 200],
        ["Hello", "", "World#123", ""],
        ["a", "b", "c"],
    ]
    
    codec1 = Codec()
    codec2 = CodecEscape()
    codec3 = CodecDelimiter()
    codec4 = CodecChunkSize()
    
    for strs in test_cases:
        # Test all codecs
        result1 = codec1.decode(codec1.encode(strs))
        result2 = codec2.decode(codec2.encode(strs))
        result3 = codec3.decode(codec3.encode(strs))
        result4 = codec4.decode(codec4.encode(strs))
        
        assert result1 == strs, f"Codec failed for {strs}: {result1}"
        assert result2 == strs, f"CodecEscape failed for {strs}: {result2}"
        assert result3 == strs, f"CodecDelimiter failed for {strs}: {result3}"
        assert result4 == strs, f"CodecChunkSize failed for {strs}: {result4}"
    
    print("  All approaches match! ✓")
    
    # Test case 12: Edge case - string starting with number
    print("\nTest 12: String starting with number - ['123abc', '456def']")
    strs12 = ["123abc", "456def"]
    encoded12 = codec.encode(strs12)
    decoded12 = codec.decode(encoded12)
    assert decoded12 == strs12, f"Test 12 failed: expected {strs12}, got {decoded12}"
    print(f"  Encoded: {encoded12}")
    print(f"  Decoded: {decoded12} ✓")
    
    # Test case 13: Many strings
    print("\nTest 13: Many strings - 100 strings")
    strs13 = [f"string{i}" for i in range(100)]
    encoded13 = codec.encode(strs13)
    decoded13 = codec.decode(encoded13)
    assert decoded13 == strs13, f"Test 13 failed"
    print(f"  Encoded length: {len(encoded13)}")
    print(f"  Decoded count: {len(decoded13)} ✓")
    
    # Test case 14: String with only '#'
    print("\nTest 14: String with only '#' - ['#', '##', '###']")
    strs14 = ["#", "##", "###"]
    encoded14 = codec.encode(strs14)
    decoded14 = codec.decode(encoded14)
    assert decoded14 == strs14, f"Test 14 failed: expected {strs14}, got {decoded14}"
    print(f"  Encoded: {encoded14}")
    print(f"  Decoded: {decoded14} ✓")
    
    # Test case 15: Very long single string
    print("\nTest 15: Very long single string - 1000 characters")
    strs15 = ["a" * 1000]
    encoded15 = codec.encode(strs15)
    decoded15 = codec.decode(encoded15)
    assert decoded15 == strs15, f"Test 15 failed"
    print(f"  Encoded length: {len(encoded15)}")
    print(f"  Decoded length: {len(decoded15[0])} ✓")
    
    print("\n" + "=" * 60)
    print("All test cases passed!")
    print("=" * 60)


if __name__ == "__main__":
    test_solution()