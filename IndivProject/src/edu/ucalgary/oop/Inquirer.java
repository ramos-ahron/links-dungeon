package edu.ucalgary.oop;

public class Inquirer extends Person {
    private String SERVICESPHONENUM;
    private String INFO;

    public Inquirer(String firstName, String lastName, String phone, String info) {
        super(firstName, lastName);
        this.SERVICESPHONENUM = phone;
        this.INFO = info;
    }

    public String getServicesPhoneNum() {
        return SERVICESPHONENUM;
    }

    public String getInfo() {
        return INFO;
    }
}


