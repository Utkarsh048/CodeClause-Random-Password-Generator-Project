import string
from random import shuffle, randint, choice


class PasswordGenerator:
    """
    Generates random passwords based on specified criteria.
    """

    def _init_(self):
        self.minlen = 6
        self.maxlen = 16
        self.minuchars = 1
        self.minlchars = 1
        self.minnumbers = 1
        self.minschars = 1
        self.excludeuchars = ""
        self.excludelchars = ""
        self.excludenumbers = ""
        self.excludeschars = ""

        self.lower_chars = string.ascii_lowercase
        self.upper_chars = string.ascii_uppercase
        self.numbers_list = string.digits
        self._schars = "!#$%^&*(),.-_+="

    def generate(self):
        """
        Generates a password using default or custom properties.
        """
        if any(
            value < 0
            for value in [
                self.minlen,
                self.maxlen,
                self.minuchars,
                self.minlchars,
                self.minnumbers,
                self.minschars,
            ]
        ):
            raise ValueError("Character length should not be negative")

        if self.minlen > self.maxlen:
            raise ValueError(
                "Minimum length cannot be greater than maximum length. The default maximum length is 16."
            )

        collective_min_length = (
            self.minuchars + self.minlchars + self.minnumbers + self.minschars
        )

        if collective_min_length > self.minlen:
            self.minlen = collective_min_length

        final_pass = [
            choice(list(set(self.lower_chars) - set(self.excludelchars)))
            for _ in range(self.minlchars)
        ]
        final_pass += [
            choice(list(set(self.upper_chars) - set(self.excludeuchars)))
            for _ in range(self.minuchars)
        ]
        final_pass += [
            choice(list(set(self.numbers_list) - set(self.excludenumbers)))
            for _ in range(self.minnumbers)
        ]
        final_pass += [
            choice(list(set(self._schars) - set(self.excludeschars)))
            for _ in range(self.minschars)
        ]

        current_pass_len = len(final_pass)
        all_chars = (
            set(self.lower_chars)
            | set(self.upper_chars)
            | set(self.numbers_list)
            | set(self._schars)
        ) - set(
            list(self.excludelchars)
            + list(self.excludeuchars)
            + list(self.excludenumbers)
            + list(self.excludeschars)
        )

        if current_pass_len < self.maxlen:
            rand_len = randint(self.minlen, self.maxlen)
            final_pass += [choice(list(all_chars)) for _ in range(rand_len - current_pass_len)]

        shuffle(final_pass)
        return "".join(final_pass)


if __name__ == "_main_":
    generator = PasswordGenerator()
    
    # Prompt user for password criteria
    generator.minlen = int(input("Enter the minimum length of the password: "))
    generator.maxlen = int(input("Enter the maximum length of the password: "))
    generator.minuchars = int(input("Enter the minimum number of uppercase characters: "))
    generator.minlchars = int(input("Enter the minimum number of lowercase characters: "))
    generator.minnumbers = int(input("Enter the minimum number of numeric characters: "))
    generator.minschars = int(input("Enter the minimum number of special characters: "))

    # Generate password based on the provided criteria
    password = generator.generate()
    print("Generated Password:",password)