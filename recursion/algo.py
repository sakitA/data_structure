def MektubCatdir(mektub_siyahi, house_number):
    # ilkin şərt hissəsi
    if house_number >= len(mektub_siyahi):
        print("Məhəlləni tərk et")
        return
    else:
        print(house_number, " nömrəli evin məktubu çatdırıldı")

        # rekursiv(təkrarlan) hissə
        MektubCatdir(mektub_siyahi, house_number + 1)  # Recursive call


if __name__ == "__main__":
    mektublar = ["Ev1", "Ev2", "Ev3"]
    MektubCatdir(mektublar, 0)