def poly_deg(p):
    """Tìm bậc của đa thức"""
    return p.bit_length() - 1 if p > 0 else -1

def poly_div(A, B):
    """Phép chia đa thức trong trường GF2"""
    Q = 0
    R = A
    deg_B = poly_deg(B)
    while poly_deg(R) >= deg_B:
        shift = poly_deg(R) - deg_B
        Q ^= (1 << shift)
        R ^= (B << shift)
    return Q, R

def poly_mul(A, B):
    """Phép nhân đa thức trong trường GF2"""
    P = 0
    while B > 0:
        if B & 1:
            P ^= A
        A <<= 1
        B >>= 1
    return P

def eea_gf2m(m, a):
    """Thuật toán Euclidean mở rộng trên GF2^m"""
    r1, r2 = m, a
    t1, t2 = 0, 1

    print(f"{'r1':<5} | {'r2':<5} | {'q':<5} | {'r':<5} | {'t1':<5} | {'t2':<5} | {'t':<5}")
    print("-" * 55)

    while r2 > 0:
        q, r = poly_div(r1, r2)
        
        t = t1 ^ poly_mul(q, t2)

        print(f"{r1:<5} | {r2:<5} | {q:<5} | {r:<5} | {t1:<5} | {t2:<5} | {t:<5}")

        r1, r2 = r2, r
        t1, t2 = t2, t

    print("-" * 55)
    return t1

m_x = 1033

print("Tìm nghịch đảo của a = 523")
inv_a = eea_gf2m(m_x, 523)
print(f"Nghịch đảo của 523 là: {inv_a}\n")

print("Tìm nghịch đảo của b = 1015")
inv_b = eea_gf2m(m_x, 1015)
print(f"Nghịch đảo của 1015 là: {inv_b}")