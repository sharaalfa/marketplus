package sharafutdinov.artur.marketplus.controller;

import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.web.authentication.logout.SecurityContextLogoutHandler;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.File;
import java.util.Collection;
import java.util.Iterator;

/**
 * Created by first on 21.03.17.
 */
@Controller
public class AppController {

    @RequestMapping(value = {"/"}, method = RequestMethod.GET)
    public ModelAndView homePage() {
        ModelAndView model = new ModelAndView();
        model.addObject("greeting", "Hi, Welcome to hello world app. ");
        model.setViewName("welcome");
        return model;
    }

    @RequestMapping(value = {"/login"}, method = RequestMethod.GET)
    public ModelAndView loginPage() {
        ModelAndView model = new ModelAndView();
        model.addObject("greeting", "Hi, Welcome to login page");
        model.setViewName("login");
        return model;
    }

    @RequestMapping(value = {"/accessdenied"}, method = RequestMethod.GET)
    public ModelAndView accessDeniedPage() {
        ModelAndView model = new ModelAndView();
        model.addObject("message", "Either username or password is incorrect.");
        model.setViewName("accessdenied");
        return model;
    }

    @RequestMapping(value = {"/userpage"}, method = RequestMethod.GET)
    public ModelAndView userPage() {

        Object principal = SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        if (principal instanceof UserDetails) {
            Collection<? extends GrantedAuthority> authorities = ((UserDetails) principal).getAuthorities();
            if (authorities.size() == 1) {
                final Iterator<? extends GrantedAuthority> iterator = authorities.iterator();
                GrantedAuthority grantedAuthority = iterator.next();
                if (grantedAuthority.getAuthority().equals("ADMIN")) {
                    return adminPage();
                }
            }
        }
        ModelAndView model = new ModelAndView();
        model.addObject("title", "Spring Security Hello World");
        model.addObject("user", getUser());
        model.setViewName("chart");
        return model;
    }



    @RequestMapping(value = "/adminpage", method = RequestMethod.GET)
    public ModelAndView adminPage() {

        ModelAndView model = new ModelAndView();
        model.addObject("title", "Spring Security Hello World");
        model.addObject("user", getUser());
        model.setViewName("admin");
        return model;
    }

    @RequestMapping(value = "/logout", method = RequestMethod.GET)
    public ModelAndView logoutPage(HttpServletRequest request, HttpServletResponse response) {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        if (auth != null) {
            new SecurityContextLogoutHandler().logout(request, response, auth);
        }
        return homePage();
    }
    @RequestMapping(value = "/chart2", method = RequestMethod.GET)
    public String registrationForm() {
        //logger.info("форма регистрации");

        return "/chart2";
    }

    @RequestMapping(value = "/data.json", method = RequestMethod.GET)
    public String chartShow(Model model) {
        try {
            File fromXml1 = new File("/home/first/data/Java_study/marketplus/data.xml");
            DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
            Document document = dBuilder.parse(fromXml1);
            document.getDocumentElement().normalize();
            NodeList nodeList = document.getElementsByTagName("doc");

            Node node = nodeList.item(0);
            Element element = (Element) node;
            double amount = Double.parseDouble(element.getElementsByTagName("field1").item(0).getTextContent());
            double amount2 = Double.parseDouble(element.getElementsByTagName("field2").item(0).getTextContent());
            String amount3= element.getElementsByTagName("field3").item(0).getTextContent();
            String amount4 = element.getElementsByTagName("field4").item(0).getTextContent();
            System.out.println(amount);
            //logger.trace("ddddd"+amount);
            model.addAttribute("errorAndOmissions1", amount);
            model.addAttribute("errorAndOmissions", amount2);
            model.addAttribute("capitalAndFlight", amount3);
            model.addAttribute("growthAndFall", amount4);

        } catch (Exception e) {
            e.printStackTrace();
        }
        return "/data";


    }

    private String getUser() {
        String userName = null;
        Object principal = SecurityContextHolder.getContext().getAuthentication().getPrincipal();
        if (principal instanceof UserDetails) {
            userName = ((UserDetails) principal).getUsername();
        } else {
            userName = principal.toString();
        }
        return userName;
    }

}
