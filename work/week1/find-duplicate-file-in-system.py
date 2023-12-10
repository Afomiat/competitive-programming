class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = {}

        for path in paths:
            parts = path.split()
            directory = parts[0]
            files = parts[1:]

            for file in files:
                file_parts = file.split('(')
                file_name = file_parts[0]
                file_content = file_parts[1][:-1]

                full_path = directory + '/' + file_name
                
                # Check if file_content is already a key in content_dict
                if file_content not in content_dict:
                    content_dict[file_content] = []

                # Append full_path to the list associated with file_content
                content_dict[file_content].append(full_path)

        result = [group for group in content_dict.values() if len(group) > 1]
        return result
