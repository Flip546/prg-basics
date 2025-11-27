def f(detector):
    detector = str(detector)
    return "+++" in detector


if __name__ == "__main__":
    print(f("------+++++---+++"))  # True
    print(f("++"))                # False
    print(f("abc+++-xyz"))        # True
    print(f("+-++-+"))            # False
