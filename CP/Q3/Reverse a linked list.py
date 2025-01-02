SinglyLinkedListNode* reverse(SinglyLinkedListNode* llist) {
    struct SinglyLinkedListNode* prev=NULL;
    struct SinglyLinkedListNode* current=llist;
    struct SinglyLinkedListNode* next=NULL;
    while(current!=NULL){
        next=current->next;
        current->next=prev;
        prev=current;
        current=next;
    }
    return prev;
}