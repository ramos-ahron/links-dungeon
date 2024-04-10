package edu.ucalgary.oop;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CentralReliefWorkerInterface {
    private static JFrame mainFrame;
    private final CentralReliefWorker centralReliefWorker = new CentralReliefWorker();
    private JTextField txtFirstName;
    private JTextField txtLastName;
    private JTextField txtName;
    private JCheckBox shelterCheckbox;
    private JTextField txtPhoneNum;
    private JTextField txtComments;
    private JTextField txtLocationAddress;
    private JTextField txtQuantity;
    private JTextField txtType;

    public static void main(String[] args) {
        if (!DatabaseInitializer.flag) {
            DatabaseInitializer.getData();
        }
        EventQueue.invokeLater(() -> {
            mainFrame = new JFrame("Central Relief Worker Interface");
            mainFrame.setSize(400, 300);
            mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            JPanel panel = new JPanel();
            mainFrame.add(panel);
            CentralReliefWorkerInterface menu = new CentralReliefWorkerInterface();
            menu.placeComponents(panel);

            mainFrame.setVisible(true);
        });
    }

    public void placeComponents(JPanel panel) {
        panel.setLayout(new GridLayout(6, 1));

        JButton switchInterfaceButton = new JButton("Switch Interface");
        JButton addInquirerButton = new JButton("Add Inquirer");
        JButton findDisasterVictimButton = new JButton("Find Disaster Victim");
        JButton getVictimRelationshipsButton = new JButton("Print Victim Relationships");
        JButton addLocationsButton = new JButton("Enter Locations");
        JButton addSupplies = new JButton("Add Supplies to Location");
        switchInterfaceButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                mainFrame.dispose();
                LocationReliefWorkerInterface locationInterface = new LocationReliefWorkerInterface();
                locationInterface.mainMenu();
            }
        });
        addInquirerButton.addActionListener(e -> {
            createAndShowGUIAddInquirer();
            mainFrame.setVisible(false);
        });
        findDisasterVictimButton.addActionListener(e -> {
            createAndShowGUIFindDisasterVictim();
            mainFrame.setVisible(false);
        });
        getVictimRelationshipsButton.addActionListener(e -> {
            createAndShowGUIVictimRelationships();
            mainFrame.setVisible(false);
        });
        addLocationsButton.addActionListener(e -> {
            createAndShowGUIAddLocation();
            mainFrame.setVisible(false);
        });
        addSupplies.addActionListener(e -> {
            createAndShowGUIAddSupply();
            mainFrame.setVisible(false);
        });
        panel.add(switchInterfaceButton);
        panel.add(addInquirerButton);
        panel.add(findDisasterVictimButton);
        panel.add(getVictimRelationshipsButton);
        panel.add(addLocationsButton);
        panel.add(addSupplies);
        mainFrame.add(panel);
        mainFrame.setVisible(true);
    }

    public void createAndShowGUIAddSupply() {
        JFrame frame = new JFrame("Enter Supply and Location Information");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel formPanel = createFormPanelAddSupply();
        JButton btnSubmit = createSubmitButtonAddSupply(frame);

        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(btnSubmit, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private JButton createSubmitButtonAddSupply(JFrame frame) {
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            if (validateFormAddSupply()) {
                submitFormAddSupply();
                frame.dispose();
                mainFrame.setVisible(true);
            }
        });
        return btnSubmit;
    }

    private JPanel createFormPanelAddSupply() {
        JPanel formPanel = new JPanel(new GridLayout(4, 2));

        formPanel.add(new JLabel("Name: "));
        txtName = new JTextField();
        formPanel.add(txtName);

        formPanel.add(new JLabel("Address: "));
        txtLocationAddress = new JTextField();
        formPanel.add(txtLocationAddress);

        formPanel.add(new JLabel("Type: "));
        txtType = new JTextField();
        formPanel.add(txtType);

        formPanel.add(new JLabel("Quantity: "));
        txtQuantity = new JTextField();
        formPanel.add(txtQuantity);

        return formPanel;
    }

    private boolean validateFormAddSupply() {
        String name = txtName.getText();
        String addressText = txtLocationAddress.getText();
        String type = txtType.getText();
        String quantity = txtQuantity.getText();

        if (name.isEmpty() || addressText.isEmpty() || type.isEmpty() || quantity.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Fill in All the text fields", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        try {
            Integer.parseInt(quantity);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Quantity should be a number", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        Location location = null;

        for (Location testLocation : ReliefService.getShelters()) {
            if (testLocation.getName().equals(name) && testLocation.getAddress().equals(addressText)) {
                location = testLocation;
            }
        }

        if (location == null) {
            JOptionPane.showMessageDialog(null, "Location is not a shelter", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        if (!ReliefService.getShelters().contains(location)) {
            JOptionPane.showMessageDialog(null, "Location is not a shelter", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        return true;
    }

    private void submitFormAddSupply() {
        Supply supply = new Supply(txtType.getText(), Integer.parseInt(txtQuantity.getText()));
        Location location = null;

        for (Location testLocation : ReliefService.getLocations()) {
            if (testLocation.getName().equals(txtName.getText()) && testLocation.getAddress().equals(txtLocationAddress.getText())) {
                location = testLocation;
            }
        }

        location.addSupply(supply);
    }

    public void createAndShowGUIAddLocation() {
        JFrame frame = new JFrame("Enter Victim Information");
        frame.setSize(400, 150);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel formPanel = createFormPanelAddLocation();
        JButton btnSubmit = createSubmitButtonAddLocation(frame);

        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(btnSubmit, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private JButton createSubmitButtonAddLocation(JFrame frame) {
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            if (validateFormAddLocation()) {
                submitFormAddLocation();
                frame.dispose();
                mainFrame.setVisible(true);
            }
        });
        return btnSubmit;
    }

    private JPanel createFormPanelAddLocation() {
        JPanel formPanel = new JPanel(new GridLayout(3, 2));

        formPanel.add(new JLabel("Name: "));
        txtName = new JTextField();
        formPanel.add(txtName);

        formPanel.add(new JLabel("Address: "));
        txtLocationAddress = new JTextField();
        formPanel.add(txtLocationAddress);

        formPanel.add(new JLabel("Shelter:"));
        shelterCheckbox = new JCheckBox();
        formPanel.add(shelterCheckbox);

        return formPanel;
    }

    private boolean validateFormAddLocation() {
        String name = txtName.getText();
        String addressText = txtLocationAddress.getText();

        if (name.isEmpty() || addressText.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Fill in All the text fields", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        return true;
    }

    private void submitFormAddLocation() {
        Location location = new Location(txtName.getText(), txtLocationAddress.getText());
        if (shelterCheckbox.isSelected()) {
            try {
                ReliefService.addShelter(location);
            } catch (IllegalArgumentException ignored) {
                JOptionPane.showMessageDialog(null, "Location already exists", "Error", JOptionPane.ERROR_MESSAGE);

            }
        }
        try {
            ReliefService.addLocation(location);
        } catch (IllegalArgumentException ignored) {
            JOptionPane.showMessageDialog(null, "Location already exists", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public void createAndShowGUIVictimRelationships() {
        JFrame frame = new JFrame("Enter Victim Information");
        frame.setSize(400, 120);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel formPanel = createFormPanelVictimRelationships();
        JButton btnSubmit = createSubmitButtonVictimRelationships(frame);

        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(btnSubmit, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private JButton createSubmitButtonVictimRelationships(JFrame frame) {
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            if (validateFormVictimRelationships()) {
                submitFormVictimRelationships();
                frame.dispose();
                mainFrame.setVisible(true);
            }
        });
        return btnSubmit;
    }

    private JPanel createFormPanelVictimRelationships() {
        JPanel formPanel = new JPanel(new GridLayout(2, 2));

        formPanel.add(new JLabel("First Name:"));
        txtFirstName = new JTextField();
        formPanel.add(txtFirstName);

        formPanel.add(new JLabel("Last Name:"));
        txtLastName = new JTextField();
        formPanel.add(txtLastName);

        return formPanel;
    }

    private boolean validateFormVictimRelationships() {
        String firstName = txtFirstName.getText();
        String lastName = txtLastName.getText();

        if (firstName.isEmpty() || lastName.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Fill in All the text fields", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        DisasterVictim victim = null;

        for (DisasterVictim disasterVictim : ReliefService.getPeople()) {
            if (disasterVictim.getFirstName().equals(firstName) && disasterVictim.getLastName().equals(lastName)) {
                victim = disasterVictim;
            }
        }

        if (victim == null) {
            JOptionPane.showMessageDialog(null, "Victim does not exist", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        return true;
    }

    private void submitFormVictimRelationships() {
        String message;
        DisasterVictim victim = new DisasterVictim("test");

        for (DisasterVictim disasterVictim : ReliefService.getPeople()) {
            if (disasterVictim.getFirstName().equals(txtFirstName.getText()) && disasterVictim.getLastName().equals(txtLastName.getText())) {
                victim = disasterVictim;
            }
        }
        message = centralReliefWorker.getRelationships(victim);
        JOptionPane.showMessageDialog(null, message, "Disaster Victims Information", JOptionPane.INFORMATION_MESSAGE);
    }

    public void createAndShowGUIFindDisasterVictim() {
        JFrame frame = new JFrame("Enter Victim Information");
        frame.setSize(400, 120);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel formPanel = createFormPanelFindDisasterVictim();
        JButton btnSubmit = createSubmitButtonFindDisasterVictim(frame);

        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(btnSubmit, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private JButton createSubmitButtonFindDisasterVictim(JFrame frame) {
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            if (validateFormFindDisasterVictim()) {
                submitFormFindDisasterVictim();
                frame.dispose();
                mainFrame.setVisible(true);
            }
        });
        return btnSubmit;
    }

    private JPanel createFormPanelFindDisasterVictim() {
        JPanel formPanel = new JPanel(new GridLayout(2, 2));

        formPanel.add(new JLabel("First Name:"));
        txtFirstName = new JTextField();
        formPanel.add(txtFirstName);

        formPanel.add(new JLabel("Last Name:"));
        txtLastName = new JTextField();
        formPanel.add(txtLastName);

        return formPanel;
    }

    private boolean validateFormFindDisasterVictim() {
        String firstName = txtFirstName.getText();
        String lastName = txtLastName.getText();

        if (firstName.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Fill in First Name text field", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }
        return true;
    }

    private void submitFormFindDisasterVictim() {
        String message;
        if (txtLastName.getText().isEmpty()) {
            message = centralReliefWorker.findDisasterVictim(txtFirstName.getText());
        } else {
            message = centralReliefWorker.findDisasterVictim(txtFirstName.getText(), txtLastName.getText());
        }

        JOptionPane.showMessageDialog(null, message, "Disaster Victims Information", JOptionPane.INFORMATION_MESSAGE);
    }

    public void createAndShowGUIAddInquirer() {
        JFrame frame = new JFrame("Enter Inquirer Information");
        frame.setSize(400, 220);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel formPanel = createFormPanelAddInquirer();
        JButton btnSubmit = createSubmitButtonAddInquirer(frame);

        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(btnSubmit, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private JButton createSubmitButtonAddInquirer(JFrame frame) {
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            if (validateFormAddInquirer()) {
                submitFormAddInquirer();
                frame.dispose();
                mainFrame.setVisible(true);
            }
        });
        return btnSubmit;
    }

    private JPanel createFormPanelAddInquirer() {
        JPanel formPanel = new JPanel(new GridLayout(4, 2));

        formPanel.add(new JLabel("First Name:"));
        txtFirstName = new JTextField();
        formPanel.add(txtFirstName);

        formPanel.add(new JLabel("Last Name:"));
        txtLastName = new JTextField();
        formPanel.add(txtLastName);

        formPanel.add(new JLabel("Phone Number:"));
        txtPhoneNum = new JTextField();
        formPanel.add(txtPhoneNum);

        formPanel.add(new JLabel("Info"));
        txtComments = new JTextField();
        formPanel.add(txtComments);

        return formPanel;
    }

    private boolean validateFormAddInquirer() {
        String firstName = txtFirstName.getText();
        String lastName = txtLastName.getText();
        String phoneNum = txtPhoneNum.getText();
        String info = txtComments.getText();

        if (firstName.isEmpty() || lastName.isEmpty() || phoneNum.isEmpty() || info.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Fill in all text fields", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        try {
            new Inquirer(firstName, lastName, phoneNum, info);
        } catch (IllegalArgumentException e) {
            JOptionPane.showMessageDialog(null, "Invalid Phone Number, follow the format 000-000-0000");
            return false;
        }

        return true;
    }

    private void submitFormAddInquirer() {
        Inquirer inquirer = new Inquirer(txtFirstName.getText(), txtLastName.getText(), txtPhoneNum.getText());
        Inquiry inquiry = new Inquiry(txtComments.getText());

        centralReliefWorker.addInquirer(inquirer, inquiry);

    }
}
