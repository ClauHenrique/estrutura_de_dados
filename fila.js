class node {
    constructor(dado){
        this.dado = dado
        this.next = null
    }
}

class queue {
    constructor(){
        this.inicio = null
        this.ultimo = null
        this.size = 0
    }

    inserir(elem){
        if (!this.inicio) {
            this.inicio = new node(elem)
            this.ultimo = this.inicio
            this.size++
        }
        else {
            let proximo = this.inicio
            // vai procurar quem e o primeiro
            // e percorrer ate achar o ultimo
            while (proximo.next) {
                proximo = proximo.next
            }
            proximo.next = new node(elem)
            this.ultimo = proximo.next
            this.size++
        }
    }
    pop(){
        let elemento = this.inicio.dado
        this.inicio = this.inicio.next
        this.size--
        console.log('tu removeu o ', elemento)
        // o elemento e removido, mas tambem  retornado
        return elemento
    }
    isEmpty(){
        if (this.size == 0) {
            return true
        }
        else return false
    }
}

const fila = new queue()
fila.inserir(2)
fila.inserir(3)
fila.inserir(4)
fila.pop()

// nao esta mais vazio
console.log(fila.isEmpty())




// console.log(fila.pop() + 5)