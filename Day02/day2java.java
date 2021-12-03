public class PasswordUncorruptor {

    private final Pattern pattern = Pattern.compile("(?<low>\\d*)-(?<high>\\d*) (?<key>[a-z]): (?<value>[a-z]*)");

    private final List<PasswordLine> passwordLines;

    public PasswordUncorruptor() {
        passwordLines = setup();
    }

    public static void main(String[] args) {
        final PasswordUncorruptor passwordUncorruptor = new PasswordUncorruptor();
        passwordUncorruptor.one();
        passwordUncorruptor.two();
    }

    public void one() {
        System.out.println(passwordLines.stream().filter(PasswordLine::isValidForOne).count());
    }

    public void two() {
        System.out.println(passwordLines.stream().filter(PasswordLine::isValidForTwo).count());
    }

    final List<PasswordLine> setup() {
        try (final BufferedReader reader = new BufferedReader(new FileReader("src/main/resources/day-two.txt"))) {
            return reader.lines().parallel().map(s -> {
                final Matcher matcher = pattern.matcher(s);
                if (!matcher.matches()) {
                    throw new IllegalStateException("Invalid Line: " + s);
                }
                return new PasswordLine(Integer.parseInt(matcher.group("low")), Integer.parseInt(matcher.group("high")),
                                        matcher.group("key").charAt(0), matcher.group("value"));
            }).collect(Collectors.toList());
        } catch (IOException e) {
            throw new IllegalStateException(e);
        }
    }

    private static final class PasswordLine {

        private final int low;
        private final int high;
        private final char key;
        private final String value;

        private PasswordLine(int low, int high, char key, String value) {
            this.low = low;
            this.high = high;
            this.key = key;
            this.value = value;
        }

        boolean isValidForOne() {
            final int matches = countMatches(value, key);
            return matches >= low && matches <= high;
        }

        boolean isValidForTwo() {
            final boolean firstPosValid = value.charAt(low - 1) == key;
            final boolean secondPosValid = value.charAt(high - 1) == key;

            if (firstPosValid) {
                return !secondPosValid;
            }
            return secondPosValid;
        }

        int countMatches(String str, char ch) {
            int count = 0;
            for (int i = 0; i < str.toCharArray().length; i++) {
                if (ch == str.charAt(i)) {
                    count++;
                }
            }
            return count;
        }
    }
}