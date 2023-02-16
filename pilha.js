class node {
    constructor(dado){
        this.dado = dado
        this.next = null
    }
}

class stack {
    constructor(){
        this.top = null
        this.size = 0
    }

    push(elem){
        let novo_elem = new node(elem)
        novo_elem.next = this.top
        this.top = novo_elem
        this.size++
    }

    pop(){
        let ultimo = this.top
        this.top = this.top.next
        console.log(ultimo.dado, 'foi removido')
        this.size--
        return ultimo
    }
    len(){
        return this.size
    }
}

const pilha = new stack()
pilha.push(5)
pilha.push(9)
pilha.push(4)
pilha.push(100)
pilha.pop()

console.log(pilha.len())