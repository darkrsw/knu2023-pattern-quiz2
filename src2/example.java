public interface DoublePredicate {}

public interface LongBiPredicate {}

public interface IntPredicate {}

public interface LongLongPredicate extends LongBiPredicate, IntPredicate {}

class MyClass implements LongLongPredicate {}
