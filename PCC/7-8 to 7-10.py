sandwich_orders = ["katsu-sando", "ham", "pastrami", "cheese", "pastrami", "pastrami"]
completed_orders = []
print(f"Oh, I can't make any pastrami. What a shame.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    done = sandwich_orders.pop()
    print(f"I've made a {done} sandwich!")
    completed_orders.append(done)
print(f"Overall I've made {completed_orders} sandwiches!")

