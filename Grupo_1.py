import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# CONFIGURACIÓN GENERAL
# ==========================================

T = 2 * np.pi
t = np.linspace(-np.pi, np.pi, 2000)

# ==========================================
# ACTIVIDAD 1
# SERIES DE FOURIER
# ==========================================

def cuadrada_original(t):
    return np.sign(np.sin(t))

def triangular_original(t):
    return (2/np.pi) * np.arcsin(np.sin(t))

def sierra_original(t):
    return t/np.pi

def rectificada_original(t):
    return np.abs(np.sin(t))


def fourier_cuadrada(t, N):
    s = np.zeros_like(t)

    for n in range(1, 2*N, 2):
        s += (4/(n*np.pi))*np.sin(n*t)

    return s


def fourier_triangular(t, N):
    s = np.zeros_like(t)

    for n in range(1, 2*N, 2):
        s += (8/(np.pi**2)) * ((-1)**((n-1)//2)) * np.sin(n*t)/(n**2)

    return s


def fourier_sierra(t, N):
    s = np.zeros_like(t)

    for n in range(1, N+1):
        s += (2/np.pi) * ((-1)**(n+1))/n * np.sin(n*t)

    return s


def fourier_rectificada(t, N):
    s = np.ones_like(t)*(2/np.pi)

    for n in range(1, N+1):
        s -= (4/np.pi)*np.cos(2*n*t)/(4*n**2 - 1)

    return s


def actividad1():

    Ns = [1,3,5,11,51]

    señales = [
        ("Onda Cuadrada", cuadrada_original, fourier_cuadrada),
        ("Onda Triangular", triangular_original, fourier_triangular),
        ("Diente de Sierra", sierra_original, fourier_sierra),
        ("|sin(t)|", rectificada_original, fourier_rectificada)
    ]

    for nombre, original, fourier in señales:

        fig, axs = plt.subplots(1,5,figsize=(18,4))

        for i,N in enumerate(Ns):

            axs[i].plot(t, original(t),'k--',label="Original")
            axs[i].plot(t, fourier(t,N),'b')

            axs[i].set_title(f"N={N}")
            axs[i].grid(True)

        fig.suptitle(nombre)
        plt.tight_layout()
        plt.show()

# ==========================================
# GIBBS
# ==========================================

def gibbs():

    plt.figure(figsize=(10,5))

    plt.plot(t, cuadrada_original(t),
             'k--',
             linewidth=3,
             label='Original')

    for N in [5,15,50]:
        plt.plot(t,
                 fourier_cuadrada(t,N),
                 label=f'N={N}')

    plt.title("Fenómeno de Gibbs")
    plt.grid(True)
    plt.legend()
    plt.show()

# ==========================================
# ACTIVIDAD 2
# ESPECTRO Y PARSEVAL
# ==========================================

def coef_cuadrada(n):

    if n == 0:
        return 0

    if n % 2 == 0:
        return 0

    return -2j/(n*np.pi)


def espectro_bilateral():

    n = np.arange(-15,16)

    c = np.array([coef_cuadrada(k) for k in n])

    plt.figure(figsize=(12,5))

    plt.subplot(1,2,1)
    plt.stem(n,np.abs(c))
    plt.title("Amplitud")
    plt.grid()

    plt.subplot(1,2,2)
    plt.stem(n,np.angle(c))
    plt.title("Fase")
    plt.grid()

    plt.tight_layout()
    plt.show()


def parseval():

    potencia_real = 1

    Ns = np.arange(1,51)

    errores = []

    for N in Ns:

        suma = 0

        for n in range(1,2*N,2):

            suma += 2*(2/(n*np.pi))**2

        error = abs(potencia_real-suma)

        errores.append(error)

    plt.semilogy(Ns,errores)

    plt.axhline(0.01,
                linestyle='--',
                color='red')

    plt.title("Convergencia Parseval")
    plt.xlabel("N")
    plt.ylabel("Error")

    plt.grid()
    plt.show()

# ==========================================
# ACTIVIDAD 3
# IMPULSO Y GAUSSIANA
# ==========================================

def impulso_gaussiana(eps):

    return np.exp(-(t**2)/eps)/np.sqrt(np.pi*eps)


def actividad3():

    plt.figure(figsize=(10,5))

    for eps in [0.1,0.01,0.001]:

        plt.plot(t,
                 impulso_gaussiana(eps),
                 label=f"eps={eps}")

    plt.title("Aproximación al impulso")
    plt.grid(True)
    plt.legend()
    plt.show()

# ==========================================
# ACTIVIDAD 4
# SIMETRIAS + DFT
# ==========================================

def simetria_oculta():

    x = np.linspace(-np.pi,np.pi,1000)

    f = 2 + np.cos(x) + np.cos(2*x)

    plt.figure(figsize=(10,5))

    plt.plot(x,f)

    plt.title("f(t)=2+cos(t)+cos(2t)")
    plt.grid(True)

    plt.show()


def dft_cuadrada():

    N = 8

    muestras = np.sign(
        np.sin(
            np.linspace(0,2*np.pi,N,endpoint=False)
        )
    )

    X = np.fft.fft(muestras)

    plt.figure(figsize=(10,5))

    plt.stem(np.arange(N),
             np.abs(X))

    plt.title("DFT de 8 puntos")
    plt.xlabel("k")
    plt.ylabel("|X[k]|")

    plt.grid(True)
    plt.show()

# ==========================================
# MENÚ PRINCIPAL
# ==========================================

while True:

    print("\n========================")
    print("PRACTICA 2 - FOURIER")
    print("========================")
    print("1. Actividad 1")
    print("2. Actividad 2")
    print("3. Actividad 3")
    print("4. Actividad 4")
    print("5. Salir")

    op = input("\nSeleccione opción: ")

    if op == "1":
        actividad1()
        gibbs()

    elif op == "2":
        espectro_bilateral()
        parseval()

    elif op == "3":
        actividad3()

    elif op == "4":
        simetria_oculta()
        dft_cuadrada()

    elif op == "5":
        break

    else:
        print("Opción inválida")