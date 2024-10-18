from extensions.prompt_inject.tests.wildcard_manager.base_wildcard_manager import BaseWildcardManagerTest


class TestWildcardManager_combos(BaseWildcardManagerTest):

    def test_AND_should_concat_multiple_wildcards(self):
        self.create_file('part1.txt', "Part1")
        self.create_file('part2.txt', "Part2")

        result = self.manager.replace_wildcard('__part1&& part2__')

        self.assertEqual('Part1Part2', result)

    def test_OR_should_return_random_wildcards(self):
        self.create_file('odd.txt', "Odd")
        self.create_file('even.txt', "Even")
        self.create_file('Ded.txt', "Ded", self.sub_dir)
        expected_values = ['Odd', 'Even', 'Ded']

        result = self.manager.replace_wildcard('__odd || even || sub/Ded__')

        self.assertIn(result, expected_values)
