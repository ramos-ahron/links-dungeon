package edu.ucalgary.oop;

import javax.swing.*;
import java.awt.*;
import java.io.IOException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.LinkedList;
import java.util.Objects;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LocationReliefWorkerInterface {
    private final LocationReliefWorker locationReliefWorker = new LocationReliefWorker();

    private static JFrame mainFrame;
    private JTextField txtFirstName;
    private JTextField txtLastName;
    private JTextField txtName;

    private JTextField txtSocialID;
    private JTextField txtEntryDate;
    private JTextField txtDateOfBirth;
    private JTextField txtComments;
    private JTextField txtLocationAddress;
    private JTextField txtType;
    private JTextField txtQuantity;
    private JComboBox<String> cmbGender;


    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            LocationReliefWorkerInterface menu = new LocationReliefWorkerInterface();
            menu.mainMenu();
        });
    }

    public void mainMenu() {
        mainFrame = new JFrame("Disaster Management System");
        mainFrame.setSize(400, 400);
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Create a panel to hold the buttons
        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(7, 1)); // Arrange buttons vertically

        // Create buttons
        JButton switchInterfaceButton = new JButton("Switch Interface");
        JButton btnPrintMissingPeople = new JButton("Print Missing People");
        JButton btnPrintDisasterVictims = new JButton("Print Disaster Victims");
        JButton btnEnterDisasterVictims = new JButton("Enter Disaster Victims");
        JButton btnRemoveDisasterVictims = new JButton("Remove Disaster Victims");
        JButton btnPrintSupplies = new JButton("Print Supplies");
        JButton btnGiveSupplies = new JButton("Give Supplies");
        JButton btnUpdateDisasterVictim = new JButton("Update Disaster Victim");

        // Add action listeners to buttons
        switchInterfaceButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                mainFrame.dispose();
                CentralReliefWorkerInterface centralInterface = new CentralReliefWorkerInterface();
                centralInterface.main(null);
            }
        });
        btnPrintMissingPeople.addActionListener(e -> printMissingPeople());
        btnPrintDisasterVictims.addActionListener(e -> {
            createAndShowGUIGetLocationDV();
            mainFrame.setVisible(false);
        });
        btnEnterDisasterVictims.addActionListener(e -> {
            createAndShowGUIEnterDV();
            mainFrame.setVisible(false); // Hide the main menu
        });
        btnRemoveDisasterVictims.addActionListener(e -> {
            createAndShowGUIRemoveDV();
            mainFrame.setVisible(false);
        });
        btnPrintSupplies.addActionListener(e -> {
            createAndShowGUIGetLocationSupplies();
            mainFrame.setVisible(false);
        });
        btnGiveSupplies.addActionListener(e -> {
            createAndShowGUIGiveSupplies();
            mainFrame.setVisible(false);
        });

        // Add buttons to the panel
        buttonPanel.add(switchInterfaceButton);
        buttonPanel.add(btnPrintMissingPeople);
        buttonPanel.add(btnPrintDisasterVictims);
        buttonPanel.add(btnEnterDisasterVictims);
        //
        buttonPanel.add(btnRemoveDisasterVictims);
        buttonPanel.add(btnPrintSupplies);
        buttonPanel.add(btnGiveSupplies);

        // Add panel to the frame
        mainFrame.add(buttonPanel);

        mainFrame.setVisible(true);
    }

    private void createAndUpdateDVMenu() {
        JFrame frame = new JFrame("Update Disaster Victim Information");
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel updatePanel = new JPanel(new GridLayout(8, 1)); // Adjust layout for update options

        JButton btnAddRelationship = new JButton("Add Relationship");
        JButton btnAddMedicalRecord = new JButton("Add Medical Record");
        JButton btnAddPersonalBelonging = new JButton("Add Personal Belonging");
        JButton btnAddDietRestrictions = new JButton("Add Diet Restrictions");
        JButton btnUpdateGender = new JButton("Update Gender");
        JButton btnUpdateComment = new JButton("Update Comment");
        JButton btnUpdateLocation = new JButton("Update Location");
        JButton btnBack = new JButton("Back to Main Menu"); // Add a back button

        // Add action listeners to update buttons
        btnAddRelationship.addActionListener(e -> {
            // Add Relationship logic here
        });
        btnAddMedicalRecord.addActionListener(e -> {
            // Add Medical Record logic here
        });
        btnAddPersonalBelonging.addActionListener(e -> {
            // Add Personal Belonging logic here
        });
        btnAddDietRestrictions.addActionListener(e -> {
            // Add Diet Restrictions logic here
        });
        btnUpdateGender.addActionListener(e -> {
            // Update Gender logic here
        });
        btnUpdateComment.addActionListener(e -> {
            // Update Comment logic here
        });
        btnUpdateLocation.addActionListener(e -> {
            // Update Location logic here
        });
        btnBack.addActionListener(e -> {
            mainFrame.setVisible(true); // Show the main menu
            frame.dispose(); // Close the current frame
        });

        // Add update buttons to the panel
        updatePanel.add(btnAddRelationship);
        updatePanel.add(btnAddMedicalRecord);
        updatePanel.add(btnAddPersonalBelonging);
        updatePanel.add(btnAddDietRestrictions);
        updatePanel.add(btnUpdateGender);
        updatePanel.add(btnUpdateComment);
        updatePanel.add(btnUpdateLocation);
        updatePanel.add(btnBack); // Add the back button

        frame.add(updatePanel, BorderLayout.CENTER);

        frame.setVisible(true);
    }

    public void createAndShowGUIRelationship() {
        JFrame frame = new JFrame("Enter Location Information");
        frame.setSize(400, 120);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel formPanel = createFormPanelRelationship();
        JButton btnSubmit = createSubmitButtonRelationship(frame); // Pass the frame as an argument

        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(btnSubmit, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private JButton createSubmitButtonRelationship(JFrame frame) { // Pass the frame as an argument
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            if (validateFormRelationship()) {
//                submitFormRelationship();
                frame.dispose(); // Close the current frame
                mainFrame.setVisible(true); // Show the main menu
            }
        });
        return btnSubmit;
    }

    private JPanel createFormPanelRelationship() {
        JPanel formPanel = new JPanel(new GridLayout(2, 2));

        formPanel.add(new JLabel("Social ID Victim 1:"));
        txtName = new JTextField();
        formPanel.add(txtName);

        formPanel.add(new JLabel("Social ID Victim 2:"));
        txtLocationAddress = new JTextField();
        formPanel.add(txtLocationAddress);

        return formPanel;
    }

    private boolean validateFormRelationship() {
        String name = txtName.getText();
        String address = txtLocationAddress.getText();

        if (name.isEmpty() || address.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Fill in all text fields", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }
        return true;
    }

    public void createAndShowGUIGetLocationDV() {
        JFrame frame = new JFrame("Enter Location Information");
        frame.setSize(400, 120);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel formPanel = createFormPanelGetLocationDV();
        JButton btnSubmit = createSubmitButtonGetLocationDV(frame); // Pass the frame as an argument

        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(btnSubmit, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private JButton createSubmitButtonGetLocationDV(JFrame frame) { // Pass the frame as an argument
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            if (validateFormGetLocation()) {
                submitFormGetLocationDV();
                frame.dispose(); // Close the current frame
                mainFrame.setVisible(true); // Show the main menu
            }
        });
        return btnSubmit;
    }

    private JPanel createFormPanelGetLocationDV() {
        JPanel formPanel = new JPanel(new GridLayout(2, 2));

        formPanel.add(new JLabel("Name:"));
        txtName = new JTextField();
        formPanel.add(txtName);

        formPanel.add(new JLabel("Address"));
        txtLocationAddress = new JTextField();
        formPanel.add(txtLocationAddress);

        return formPanel;
    }

    public void createAndShowGUIGetLocationSupplies() {
        JFrame frame = new JFrame("Enter Location Information");
        frame.setSize(400, 120);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel formPanel = createFormPanelGetLocationSupplies();
        JButton btnSubmit = createSubmitButtonGetLocationSupplies(frame); // Pass the frame as an argument

        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(btnSubmit, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private JButton createSubmitButtonGetLocationSupplies(JFrame frame) { // Pass the frame as an argument
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            if (validateFormGetLocation()) {
                submitFormGetLocationSupplies();
                frame.dispose(); // Close the current frame
                mainFrame.setVisible(true); // Show the main menu
            }
        });
        return btnSubmit;
    }

    private JPanel createFormPanelGetLocationSupplies() {
        JPanel formPanel = new JPanel(new GridLayout(2, 2));

        formPanel.add(new JLabel("Name:"));
        txtName = new JTextField(); // Initialize txtType
        formPanel.add(txtName);

        formPanel.add(new JLabel("Address"));
        txtLocationAddress = new JTextField(); // Initialize txtQuantity
        formPanel.add(txtLocationAddress);

        return formPanel;
    }

    private boolean validateFormGetLocation() {
        String name = txtName.getText();
        String address = txtLocationAddress.getText();

        if (name.isEmpty() || address.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Fill in all text fields", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }
        return true;
    }

    public void createAndShowGUIGiveSupplies() {
        JFrame frame = new JFrame("Enter Supplies Information");
        frame.setSize(400, 150);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel formPanel = createFormPanelGiveSupplies();
        JButton btnSubmit = createSubmitButtonGiveSupplies(frame); // Pass the frame as an argument

        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(btnSubmit, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private JButton createSubmitButtonGiveSupplies(JFrame frame) { // Pass the frame as an argument
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            if (validateFormGiveSupplies()) {
                submitFormGiveSupplies();
                frame.dispose(); // Close the current frame
                mainFrame.setVisible(true); // Show the main menu
            }
        });
        return btnSubmit;
    }

    private JPanel createFormPanelGiveSupplies() {
        JPanel formPanel = new JPanel(new GridLayout(3, 2));

        formPanel.add(new JLabel("Type:"));
        txtType = new JTextField(); // Initialize txtType
        formPanel.add(txtType);

        formPanel.add(new JLabel("Quantity"));
        txtQuantity = new JTextField(); // Initialize txtQuantity
        formPanel.add(txtQuantity);

        formPanel.add(new JLabel("Social ID:"));
        txtSocialID = new JTextField(); // Initialize txtSocialID
        formPanel.add(txtSocialID);

        return formPanel;
    }

    private boolean validateFormGiveSupplies() {
        String type = txtType.getText();
        String quantity = txtQuantity.getText();
        String id = txtSocialID.getText();

        if (type.isEmpty() || quantity.isEmpty() || id.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Fill in all text fields", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }
        try {
            Integer.parseInt(quantity);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Quantity should be a number", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }
        try {
            Integer.parseInt(id);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Social ID should be a number", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        DisasterVictim person = null;

        for (DisasterVictim victim : ReliefService.getPeople()) {
            if (victim.getAssignedSocialID() == Integer.parseInt(id)) {
                person = victim;
            }
        }

        if (person == null) {
            JOptionPane.showMessageDialog(null, "No Victim with information provided exists", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        return true;
    }

    public void createAndShowGUIRemoveDV() {
        JFrame frame = new JFrame("Enter Disaster Victim to Remove Information");
        frame.setSize(400, 150);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel formPanel = createFormPanelRemoveDV();
        JButton btnSubmit = createSubmitButtonRemoveDV(frame); // Pass the frame as an argument

        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(btnSubmit, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private JButton createSubmitButtonRemoveDV(JFrame frame) { // Pass the frame as an argument
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            if (validateFormRemoveDV()) {
                submitFormRemoveDV();
                frame.dispose(); // Close the current frame
                mainFrame.setVisible(true); // Show the main menu
            }
        });
        return btnSubmit;
    }

    private boolean validateFormRemoveDV() {
        String firstName = txtFirstName.getText();
        String lastName = txtLastName.getText();
        String id = txtSocialID.getText();

        if (firstName.isEmpty() || lastName.isEmpty() || id.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Fill in all text fields", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }
        try {
            Integer.parseInt(id);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Social ID should be a number", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        DisasterVictim person = null;

        for (DisasterVictim victim : ReliefService.getPeople()) {
            if (victim.getAssignedSocialID() == Integer.parseInt(id) && Objects.equals(victim.getFirstName(), firstName) && Objects.equals(victim.getLastName(), lastName)) {
                person = victim;
            }
        }

        if (person == null) {
            JOptionPane.showMessageDialog(null, "No Victim with information provided exists", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        return true;
    }

    private JPanel createFormPanelRemoveDV() {
        JPanel formPanel = new JPanel(new GridLayout(3, 2));

        formPanel.add(new JLabel("First Name:"));
        txtFirstName = new JTextField();
        formPanel.add(txtFirstName);

        formPanel.add(new JLabel("Last Name:"));
        txtLastName = new JTextField();
        formPanel.add(txtLastName);

        formPanel.add(new JLabel("Social ID:"));
        txtSocialID = new JTextField();
        formPanel.add(txtSocialID);

        return formPanel;
    }

    public void createAndShowGUIEnterDV() {
        JFrame frame = new JFrame("Enter Disaster Victim Information");
        frame.setSize(400, 340);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel formPanel = createFormPanelEnterDV();
        JButton btnSubmit = createSubmitButtonEnterDV(frame); // Pass the frame as an argument

        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(btnSubmit, BorderLayout.SOUTH);

        frame.setVisible(true);
    }

    private JPanel createFormPanelEnterDV() {
        JPanel formPanel = new JPanel(new GridLayout(8, 2));

        formPanel.add(new JLabel("First Name:"));
        txtFirstName = new JTextField();
        formPanel.add(txtFirstName);

        formPanel.add(new JLabel("Last Name:"));
        txtLastName = new JTextField();
        formPanel.add(txtLastName);

        formPanel.add(new JLabel("Entry Date:"));
        txtEntryDate = new JTextField();
        formPanel.add(txtEntryDate);

        formPanel.add(new JLabel("Date of Birth:"));
        txtDateOfBirth = new JTextField();
        formPanel.add(txtDateOfBirth);

        formPanel.add(new JLabel("Comments:"));
        txtComments = new JTextField();
        formPanel.add(txtComments);

        formPanel.add(new JLabel("Location Name:"));
        txtName = new JTextField();
        formPanel.add(txtName);

        formPanel.add(new JLabel("Location Address:"));
        txtLocationAddress = new JTextField();
        formPanel.add(txtLocationAddress);

        formPanel.add(new JLabel("Gender:"));
        GenderOption options = new GenderOption("./src/edu/ucalgary/oop/GenderOptions.txt");
        String[] genders = null;
        try {
            genders = options.getOptions().toArray(new String[0]);
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, "GenderOptions.txt is in the wrong file directory", "Error", JOptionPane.ERROR_MESSAGE);
        }
        cmbGender = new JComboBox<>(genders);
        formPanel.add(cmbGender);

        return formPanel;
    }

    private JButton createSubmitButtonEnterDV(JFrame frame) { // Pass the frame as an argument
        JButton btnSubmit = new JButton("Submit");
        btnSubmit.addActionListener(e -> {
            if (validateForm()) {
                submitFormEnterDV();
                frame.dispose(); // Close the current frame
                mainFrame.setVisible(true); // Show the main menu
            }
        });
        return btnSubmit;
    }

    private boolean validateForm() {
        String firstName = txtFirstName.getText();
        String lastName = txtLastName.getText();
        String entryDate = txtEntryDate.getText();
        String dateOfBirth = txtDateOfBirth.getText();
        String name = txtName.getText();
        String address = txtLocationAddress.getText();

        // Validate first name and last name
        if (firstName.isEmpty() || lastName.isEmpty()) {
            JOptionPane.showMessageDialog(null, "First Name and Last Name are required.", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        if (name.isEmpty() || address.isEmpty()) {
            JOptionPane.showMessageDialog(null, "Location Name and Address are required.", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        // Validate entry date format
        try {
            LocalDate parsedEntryDate = LocalDate.parse(entryDate, DateTimeFormatter.ISO_LOCAL_DATE);
            LocalDate currentDate = LocalDate.now();
            if (parsedEntryDate.isAfter(currentDate)) {
                JOptionPane.showMessageDialog(null, "Entry Date cannot be in the future.", "Error", JOptionPane.ERROR_MESSAGE);
                return false;
            }
        } catch (DateTimeParseException ex) {
            JOptionPane.showMessageDialog(null, "Invalid Entry Date. Please enter a date in the format yyyy-mm-dd.", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        // Validate date of birth format
        try {
            LocalDate.parse(dateOfBirth, DateTimeFormatter.ISO_LOCAL_DATE);
        } catch (DateTimeParseException ex) {
            JOptionPane.showMessageDialog(null, "Invalid Date of Birth. Please enter a date in the format yyyy-mm-dd.", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

        return true;
    }

    private void submitFormEnterDV() {
        String firstName = txtFirstName.getText();
        String lastName = txtLastName.getText();
        String entryDateText = txtEntryDate.getText();
        LocalDate entryDate = null;
        try {
            entryDate = LocalDate.parse(entryDateText);
        } catch (DateTimeParseException ignored) {
        }

        // Check if other fields are empty
        if (firstName.isEmpty()) {
            JOptionPane.showMessageDialog(null, "First Name is required.", "Error", JOptionPane.ERROR_MESSAGE);
        }

        // Construct DisasterVictim object based on available information
        DisasterVictim victim;
        if (!lastName.isEmpty()) {
            if (!entryDateText.isEmpty()) {
                victim = new DisasterVictim(firstName, lastName, entryDateText);
            } else {
                victim = new DisasterVictim(firstName, lastName);
            }
        } else {
            victim = new DisasterVictim(firstName);
        }

        if (!txtDateOfBirth.getText().isEmpty()) {
            victim.setDateOfBirth(txtDateOfBirth.getText());
        }
        if (!txtComments.getText().isEmpty()) {
            victim.setComments(txtComments.getText());
        }
        Location location = new Location(txtName.getText(), txtLocationAddress.getText());
        System.out.println(location.getName());
        try {
            locationReliefWorker.addDisasterVictim(victim, location);
        } catch (IllegalArgumentException e) {
            JOptionPane.showMessageDialog(null, "Victim is already in location.", "Error", JOptionPane.ERROR_MESSAGE);
        }

        String selectedGender = (String) cmbGender.getSelectedItem();
        try {
            victim.setGender(selectedGender);
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, "GenderOptions.txt is in the wrong file directory", "Error", JOptionPane.ERROR_MESSAGE);

        }
    }

    private void submitFormRemoveDV() {
        String firstName = txtFirstName.getText();
        String lastName = txtLastName.getText();
        int id = Integer.parseInt(txtSocialID.getText());

        DisasterVictim person = null;

        for (DisasterVictim victim : ReliefService.getPeople()) {
            if (victim.getAssignedSocialID() == id && Objects.equals(victim.getFirstName(), firstName) && Objects.equals(victim.getLastName(), lastName)) {
                person = victim;
            }
        }

        try {
            locationReliefWorker.removeDisasterVictim(person);
        } catch (Exception ignored) {

        }
    }

    private void submitFormGiveSupplies() {
        String type = txtType.getText();
        int quantity = Integer.parseInt(txtQuantity.getText());
        int id = Integer.parseInt(txtSocialID.getText());

        DisasterVictim person = null;

        for (DisasterVictim victim : ReliefService.getPeople()) {
            if (victim.getAssignedSocialID() == id) {
                person = victim;
            }
        }

        try {
            locationReliefWorker.giveSupplies(person, new Supply(type, quantity));
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, person.getFirstName() + " " + person.getLastName() + " is currently missing and cannot be given supplies", "Error", JOptionPane.ERROR_MESSAGE);

        }
    }

    private void submitFormGetLocationDV() {
        String name = txtName.getText();
        String address = txtLocationAddress.getText();

        Location place = null;

        for (Location location : ReliefService.getLocations()) {
            if (location.getAddress().equals(address) && location.getName().equals(name)) {
                place = location;
            }
        }

        StringBuilder message = new StringBuilder();
        try {
            for (DisasterVictim victim : place.getOccupants()) {
                message.append(victim.getInfo());
            }
        } catch (Exception ignored) {

        }

        if (message.length() == 0) {
            message.append("There are no missing people");
        }

        JOptionPane.showMessageDialog(null, message.toString(), "Disaster Victims Information", JOptionPane.INFORMATION_MESSAGE);
    }

    private void submitFormGetLocationSupplies() {
        String name = txtName.getText();
        String address = txtLocationAddress.getText();

        Location location = null;

        for (Location place : ReliefService.getLocations()) {
            if (place.getAddress().equals(address) && place.getName().equals(name)) {
                location = place;
            }
        }

        if (location == null) {
            JOptionPane.showMessageDialog(null, location.getName() + " is currently not considered a shelter and thus does not have supplies", "Error", JOptionPane.ERROR_MESSAGE);
        } else {
            StringBuilder message = new StringBuilder();
            for (Supply supply : location.getSupplies()) {
                message.append("Type: ").append(supply.getType()).append(", Quantity: ").append(supply.getQuantity()).append("\n\n");
            }
            JOptionPane.showMessageDialog(null, message.toString(), "Disaster Victims Information", JOptionPane.INFORMATION_MESSAGE);
        }
    }

    private void printMissingPeople() {
        System.out.println("Print Missing People function called.");
        LinkedList<DisasterVictim> missingPeople = ReliefService.getMissingPeople();

        StringBuilder message = new StringBuilder();
        for (DisasterVictim victim : missingPeople) {
            message.append(victim.getInfo());
        }

        if (message.length() == 0) {
            message.append("There are no missing people");
        }

        JOptionPane.showMessageDialog(null, message.toString(), "Disaster Victims Information", JOptionPane.INFORMATION_MESSAGE);
    }
}
