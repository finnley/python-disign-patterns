import context
import concrete_strategy_a, concrete_strategy_b, concrete_strategy_c


# 由于实例化不同的策略，所以最终在调用听你 context.context_interface() 时，所获得的结果就不尽相同
class Program:
    context = context.Context(concrete_strategy_a.ConcreteStrategyA())
    context.context_interface()

    context = context.Context(concrete_strategy_b.ConcreteStrategyB())
    context.context_interface()

    context = context.Context(concrete_strategy_c.ConcreteStrategyC())
    context.context_interface()
